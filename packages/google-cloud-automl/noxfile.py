# -*- coding: utf-8 -*-
#
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by synthtool. DO NOT EDIT!

from __future__ import absolute_import
import os
import pathlib
import re
import shutil
import warnings

import nox

BLACK_VERSION = "black==22.3.0"
ISORT_VERSION = "isort==5.10.1"
LINT_PATHS = ["docs", "google", "tests", "noxfile.py", "setup.py"]

DEFAULT_PYTHON_VERSION = "3.8"

UNIT_TEST_PYTHON_VERSIONS = ["3.7", "3.8", "3.9", "3.10", "3.11"]
UNIT_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "asyncmock",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
]
UNIT_TEST_EXTERNAL_DEPENDENCIES = []
UNIT_TEST_LOCAL_DEPENDENCIES = []
UNIT_TEST_DEPENDENCIES = []
UNIT_TEST_EXTRAS = [
    "pandas",
    "storage",
]
UNIT_TEST_EXTRAS_BY_PYTHON = {}

SYSTEM_TEST_PYTHON_VERSIONS = ["3.8"]
SYSTEM_TEST_STANDARD_DEPENDENCIES = [
    "mock",
    "pytest",
    "google-cloud-testutils",
]
SYSTEM_TEST_EXTERNAL_DEPENDENCIES = []
SYSTEM_TEST_LOCAL_DEPENDENCIES = []
SYSTEM_TEST_DEPENDENCIES = []
SYSTEM_TEST_EXTRAS = [
    "pandas",
    "storage",
]
SYSTEM_TEST_EXTRAS_BY_PYTHON = {}

CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()

# 'docfx' is excluded since it only needs to run in 'docs-presubmit'
nox.options.sessions = [
    "unit",
    "system",
    "cover",
    "lint",
    "lint_setup_py",
    "blacken",
    "docs",
]

# Error if a python version is missing
nox.options.error_on_missing_interpreters = True


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint(session):
    """Run linters.

    Returns a failure if the linters find linting errors or sufficiently
    serious code quality issues.
    """
    session.install("flake8", BLACK_VERSION)
    session.run(
        "black",
        "--check",
        *LINT_PATHS,
    )
    session.run("flake8", "google", "tests")


@nox.session(python=DEFAULT_PYTHON_VERSION)
def blacken(session):
    """Run black. Format code to uniform standard."""
    session.install(BLACK_VERSION)
    session.run(
        "black",
        *LINT_PATHS,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def format(session):
    """
    Run isort to sort imports. Then run black
    to format code to uniform standard.
    """
    session.install(BLACK_VERSION, ISORT_VERSION)
    # Use the --fss option to sort imports using strict alphabetical order.
    # See https://pycqa.github.io/isort/docs/configuration/options.html#force-sort-within-sections
    session.run(
        "isort",
        "--fss",
        *LINT_PATHS,
    )
    session.run(
        "black",
        *LINT_PATHS,
    )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def lint_setup_py(session):
    """Verify that setup.py is valid (including RST check)."""
    session.install("docutils", "pygments")
    session.run("python", "setup.py", "check", "--restructuredtext", "--strict")


def install_unittest_dependencies(session, *constraints):
    standard_deps = UNIT_TEST_STANDARD_DEPENDENCIES + UNIT_TEST_DEPENDENCIES
    session.install(*standard_deps, *constraints)

    if UNIT_TEST_EXTERNAL_DEPENDENCIES:
        warnings.warn(
            "'unit_test_external_dependencies' is deprecated. Instead, please "
            "use 'unit_test_dependencies' or 'unit_test_local_dependencies'.",
            DeprecationWarning,
        )
        session.install(*UNIT_TEST_EXTERNAL_DEPENDENCIES, *constraints)

    if UNIT_TEST_LOCAL_DEPENDENCIES:
        session.install(*UNIT_TEST_LOCAL_DEPENDENCIES, *constraints)

    if UNIT_TEST_EXTRAS_BY_PYTHON:
        extras = UNIT_TEST_EXTRAS_BY_PYTHON.get(session.python, [])
    elif UNIT_TEST_EXTRAS:
        extras = UNIT_TEST_EXTRAS
    else:
        extras = []

    if extras:
        session.install("-e", f".[{','.join(extras)}]", *constraints)
    else:
        session.install("-e", ".", *constraints)


def default(session):
    # Install all test dependencies, then install this package in-place.

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    install_unittest_dependencies(session, "-c", constraints_path)

    # Run py.test against the unit tests.
    session.run(
        "py.test",
        "--quiet",
        f"--junitxml=unit_{session.python}_sponge_log.xml",
        "--cov=google",
        "--cov=tests/unit",
        "--cov-append",
        "--cov-config=.coveragerc",
        "--cov-report=",
        "--cov-fail-under=0",
        os.path.join("tests", "unit"),
        *session.posargs,
    )


@nox.session(python=UNIT_TEST_PYTHON_VERSIONS)
def unit(session):
    """Run the unit test suite."""
    default(session)


def install_systemtest_dependencies(session, *constraints):

    # Use pre-release gRPC for system tests.
    # Exclude version 1.52.0rc1 which has a known issue.
    # See https://github.com/grpc/grpc/issues/32163
    session.install("--pre", "grpcio!=1.52.0rc1")

    session.install(*SYSTEM_TEST_STANDARD_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_EXTERNAL_DEPENDENCIES:
        session.install(*SYSTEM_TEST_EXTERNAL_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_LOCAL_DEPENDENCIES:
        session.install("-e", *SYSTEM_TEST_LOCAL_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_DEPENDENCIES:
        session.install("-e", *SYSTEM_TEST_DEPENDENCIES, *constraints)

    if SYSTEM_TEST_EXTRAS_BY_PYTHON:
        extras = SYSTEM_TEST_EXTRAS_BY_PYTHON.get(session.python, [])
    elif SYSTEM_TEST_EXTRAS:
        extras = SYSTEM_TEST_EXTRAS
    else:
        extras = []

    if extras:
        session.install("-e", f".[{','.join(extras)}]", *constraints)
    else:
        session.install("-e", ".", *constraints)


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def system(session):
    """Run the system test suite."""
    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )
    system_test_path = os.path.join("tests", "system.py")
    system_test_folder_path = os.path.join("tests", "system")

    # Check the value of `RUN_SYSTEM_TESTS` env var. It defaults to true.
    if os.environ.get("RUN_SYSTEM_TESTS", "true") == "false":
        session.skip("RUN_SYSTEM_TESTS is set to false, skipping")
    # Install pyopenssl for mTLS testing.
    if os.environ.get("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false") == "true":
        session.install("pyopenssl")

    system_test_exists = os.path.exists(system_test_path)
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    # Sanity check: only run tests if found.
    if not system_test_exists and not system_test_folder_exists:
        session.skip("System tests were not found")

    install_systemtest_dependencies(session, "-c", constraints_path)

    # Run py.test against the system tests.
    if system_test_exists:
        session.run(
            "py.test",
            "--quiet",
            f"--junitxml=system_{session.python}_sponge_log.xml",
            system_test_path,
            *session.posargs,
        )
    if system_test_folder_exists:
        session.run(
            "py.test",
            "--quiet",
            f"--junitxml=system_{session.python}_sponge_log.xml",
            system_test_folder_path,
            *session.posargs,
        )


@nox.session(python=DEFAULT_PYTHON_VERSION)
def cover(session):
    """Run the final coverage report.

    This outputs the coverage report aggregating coverage from the unit
    test runs (not system test runs), and then erases coverage data.
    """
    session.install("coverage", "pytest-cov")
    session.run("coverage", "report", "--show-missing", "--fail-under=99")

    session.run("coverage", "erase")


@nox.session(python="3.9")
def docs(session):
    """Build the docs for this library."""

    session.install("-e", ".")
    session.install(
        "sphinx==4.0.1",
        "alabaster",
        "recommonmark",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-W",  # warnings as errors
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )


@nox.session(python="3.9")
def docfx(session):
    """Build the docfx yaml files for this library."""

    session.install("-e", ".")
    session.install(
        "gcp-sphinx-docfx-yaml",
        "alabaster",
        "recommonmark",
    )

    shutil.rmtree(os.path.join("docs", "_build"), ignore_errors=True)
    session.run(
        "sphinx-build",
        "-T",  # show full traceback on exception
        "-N",  # no colors
        "-D",
        (
            "extensions=sphinx.ext.autodoc,"
            "sphinx.ext.autosummary,"
            "docfx_yaml.extension,"
            "sphinx.ext.intersphinx,"
            "sphinx.ext.coverage,"
            "sphinx.ext.napoleon,"
            "sphinx.ext.todo,"
            "sphinx.ext.viewcode,"
            "recommonmark"
        ),
        "-b",
        "html",
        "-d",
        os.path.join("docs", "_build", "doctrees", ""),
        os.path.join("docs", ""),
        os.path.join("docs", "_build", "html", ""),
    )


@nox.session(python=SYSTEM_TEST_PYTHON_VERSIONS)
def prerelease_deps(session):
    """Run all tests with prerelease versions of dependencies installed."""

    # Install all dependencies
    session.install("-e", ".[all, tests, tracing]")
    unit_deps_all = UNIT_TEST_STANDARD_DEPENDENCIES + UNIT_TEST_EXTERNAL_DEPENDENCIES
    session.install(*unit_deps_all)
    system_deps_all = (
        SYSTEM_TEST_STANDARD_DEPENDENCIES + SYSTEM_TEST_EXTERNAL_DEPENDENCIES
    )
    session.install(*system_deps_all)

    # Because we test minimum dependency versions on the minimum Python
    # version, the first version we test with in the unit tests sessions has a
    # constraints file containing all dependencies and extras.
    with open(
        CURRENT_DIRECTORY
        / "testing"
        / f"constraints-{UNIT_TEST_PYTHON_VERSIONS[0]}.txt",
        encoding="utf-8",
    ) as constraints_file:
        constraints_text = constraints_file.read()

    # Ignore leading whitespace and comment lines.
    constraints_deps = [
        match.group(1)
        for match in re.finditer(
            r"^\s*(\S+)(?===\S+)", constraints_text, flags=re.MULTILINE
        )
    ]

    session.install(*constraints_deps)

    prerel_deps = [
        "protobuf",
        # dependency of grpc
        "six",
        "googleapis-common-protos",
        # Exclude version 1.52.0rc1 which has a known issue. See https://github.com/grpc/grpc/issues/32163
        "grpcio!=1.52.0rc1",
        "grpcio-status",
        "google-api-core",
        "google-auth",
        "proto-plus",
        "google-cloud-testutils",
        # dependencies of google-cloud-testutils"
        "click",
    ]

    for dep in prerel_deps:
        session.install("--pre", "--no-deps", "--upgrade", dep)

    # Remaining dependencies
    other_deps = [
        "requests",
    ]
    session.install(*other_deps)

    # Print out prerelease package versions
    session.run(
        "python", "-c", "import google.protobuf; print(google.protobuf.__version__)"
    )
    session.run("python", "-c", "import grpc; print(grpc.__version__)")
    session.run("python", "-c", "import google.auth; print(google.auth.__version__)")

    session.run("py.test", "tests/unit")

    system_test_path = os.path.join("tests", "system.py")
    system_test_folder_path = os.path.join("tests", "system")

    # Only run system tests if found.
    if os.path.exists(system_test_path):
        session.run(
            "py.test",
            "--verbose",
            f"--junitxml=system_{session.python}_sponge_log.xml",
            system_test_path,
            *session.posargs,
        )
    if os.path.exists(system_test_folder_path):
        session.run(
            "py.test",
            "--verbose",
            f"--junitxml=system_{session.python}_sponge_log.xml",
            system_test_folder_path,
            *session.posargs,
        )
