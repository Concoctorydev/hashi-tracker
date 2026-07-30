# Test Plan — Signup

## Test Cases

| ID    | Test Case                | Steps                                                                                        | Expected Result                                                              | Actual Result | Status     |
| ----- | ------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------- | ---------- |
| TC-01 | Successful signup        | Enter valid email, unique username, matching passwords (8-12 chars). Submit.                 | Account created; confirmation message shown.                                 |Account created| ✅ Pass |
| TC-02 | Mismatched passwords     | Enter valid email/username, different values in password and repeat-password fields. Submit. | Error: "Passwords do not match. Please go back and try again."               |               | ⬜ Not Run |
| TC-03 | Duplicate email          | Sign up with an email already registered, new username. Submit.                              | Error: "That email is already registered. Please go back and try again."     |               | ⬜ Not Run |
| TC-04 | Duplicate username       | Sign up with a username already registered, new email. Submit.                               | Error: "That username is already taken. Please go back and try again."       |               | ⬜ Not Run |
| TC-05 | Empty required field(s)  | Leave one or more fields blank. Submit.                                                      | Form should not submit / validation error shown.                             |               | ⬜ Not Run |
| TC-06 | Password stored securely | Complete a successful signup. Inspect `hashitracker.db` directly.                            | `password_hash` column contains a hashed value, not the plain-text password. |               | ⬜ Not Run |

## Bug Log

| ID  | Description | Steps to Reproduce | Expected vs. Actual | Severity | Status |
| --- | ----------- | ------------------ | ------------------- | -------- | ------ |
|BUG-01|Signup fails; AttributeError: module 'hashlib' has no attribute 'scrypt'|Submit signup form successfully|Expected: Successful account creation. Actual: 500 error/server crash|Critical; broken signup|Fixed by specifying method 'pbkdf2:sha256' for password hashing|

## Notes

- Status legend: ⬜ Not Run · ✅ Pass · ❌ Fail
- Update "Actual Result" and "Status" columns as each test case is run.
- Log any discovered bugs in the Bug Log table above, even if a related test case passes overall.
