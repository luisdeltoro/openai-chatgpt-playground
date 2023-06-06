# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This target sets the metadata for all the Python non-test files in this directory.
#
# * Pants cannot yet infer dependencies on `resource` / `resources` targets, so we explicitly add
#   the dep.
python_sources(
    name="lib",
    dependencies=[":env"],
)

# This target sets the metadata for all the Python test files in this directory.
python_tests(
    name="tests",
)

# This target teaches Pants about our .env file, which allows other targets to depend on it.
resource(
    name="env",
    source=".env",
)
