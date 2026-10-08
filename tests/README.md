# QA Test Notes

## Test Objective

Verify that the repository scanner detects AI-related source-code patterns across
multiple programming languages and file types.

## Suggested Test

1. Scan the repository.
2. Confirm the scanner reports findings from `src/`.
3. Compare the detected patterns with `scanner-fixtures/keyword-catalog.txt`.
4. Verify duplicate occurrences are handled correctly.
5. Verify source-code context/file path is shown in the finding.
6. Verify the scanner does not treat ordinary unrelated text as an AI integration.
