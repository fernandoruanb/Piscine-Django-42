#!/bin/sh

# -e -> errexit -> if something does not work, fail immediately
# -u -> unset -> if not exists fail

set -eu

die() { printf '%s\n' "Error: $*" >&2; exit 1; }

# Valid commentaries in sh shell using heredoc

: <<'DOC'
	That script receives an URL from BitLy and identify the real target consulting
	directly the BitLy server and get the Location header
DOC

# $# indicates the quantity of arguments

[ "$#" -ne 1 ] && die "usage: $0 <url>"

command -v curl > /dev/null 2>&1 || die "curl not found"

output=$(curl -sI "$1" | grep -E '^Location:[[:space:]]' | cut -d ' ' -f 2)

echo "$output"
