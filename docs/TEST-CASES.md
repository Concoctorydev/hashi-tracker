# Test Plan — Signup

## Test Cases

| ID    | Test Case                | Steps                                                                                        | Expected Result                                                              | Actual Result | Status     |
| ----- | ------------------------ | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------- | ---------- |
| TC-01 | Successful signup  | Enter valid email, unique username, matching passwords (8-12 chars). Submit.  | Account created; confirmation message shown.  |Account created| ✅ Pass |
| TC-02 | Mismatched passwords     | Enter valid email/username, different values in password and repeat-password fields. Submit. | Error: "Passwords do not match. Please go back and try again."|Validation error returned with expected error message| ✅ Pass |
| TC-03 | Duplicate email          | Sign up with an email already registered, new username. Submit.| Error: "That email is already registered. Please go back and try again."     |Validation error returned with expected error message| ✅ Pass |
| TC-04 | Duplicate username       | Sign up with a username already registered, new email. Submit.| Error: "That username is already taken. Please go back and try again."       |Validation error returned with expected error message| ✅ Pass |
| TC-05 | Empty required field(s)  | Leave one or more fields blank. Submit. | Form should not submit / validation error shown. |Form submission fails with empty input fields, validation error returns| ✅ Pass |
| TC-06 | Password stored securely | Complete a successful signup. Inspect `hashitracker.db` directly. | `password_hash` column contains a hashed value, not the plain-text password. |Confirmed password_hash column in users table contains properly hashed values.Verified via DB Browser.| ✅ Pass |
**Note:** While verifying password hashing via DB Browser, leftover test rows from TC-02 found with empty data fields. Cleared with 'DELETE FROM users;'.
| TC-07 | Password complexity requirements.  |Enter a password shorter than 8 characters, longer than 14 characters or one with no numbers/no letters. Submit. | Error message indicating password requirements not met.    | Validation error if password requirements are not met.   | ✅ Pass|
**Note:** During validation testing for password requirements, max-length password test appeared to fail due to client-side maxlength attribute preventing direct field input of more that 14 characters. Removed attribute, validated testing, all tests passed and attribute restored. 
| TC-08 | SQL injection attempt | Enter ' OR '1'='1, ' OR '1'='1' --, admin'--, ' OR 1=1 --, and '; DROP TABLE users; --  in email/username/password fields. Submit. | Input treated as literal text; no unexpected database behavior, no error exposing SQL. | Tested each SQL injection payload across email, username, and password via curl to bypass client-side validation. Signup successful for each test, with each SQL injection payload being treated as literal text. No injection occurred and no data was lost; users table remained intact and all password fields were properly hashed, verified via direct database inspection. | ✅ Pass |
| TC-09 | Special characters / unicode input | Enter emoji or symbols (🎉, @, #) in username. Then separately test accented/non-Latin characters (é, 名前). Submit each. | Emoji/symbols rejected with a validation error. Accented and non-Latin characters accepted and stored correctly. |      | ⬜ Not Run |
| TC-10 | Case sensitivity in email/username uniqueness | Sign up with email of different case but same value, then test again with username with different case and same value. Submit each. |Rejected as duplicate; email and username uniqueness checks are case-insensitive. |      | ⬜ Not Run |
| TC-11 | Leading/trailing whitespace in fields | Enter username with spaces before and after, submit. Test again with email and password. Submit. | Whitespace is trimmed before storage; account created with username stored with no leading/trailing spaces. |      | ⬜ Not Run |
| TC-12 | Invalid email format | Enter a malformed email (e.g. notanemail, missing@domain). Submit. | Error message indicating invalid email format. |      | ⬜ Not Run |
| TC-13 | Cross-site scripting (XSS) attempt | Enter <script>alert('test')</script> in username. Submit. | Input treated as literal text when displayed anywhere; script does not execute. |      | ⬜ Not Run |


## Bug Log

| ID  | Description | Steps to Reproduce | Expected vs. Actual | Severity | Status |
| --- | ----------- | ------------------ | ------------------- | -------- | ------ |
|BUG-01|Signup fails; AttributeError: module 'hashlib' has no attribute 'scrypt'|Submit signup form successfully|Expected: Successful account creation. Actual: 500 error/server crash|Critical; broken signup|Fixed by specifying method 'pbkdf2:sha256' for password hashing|
|BUG-02|Signup successful with missing input in required fields|Submit signup form with missing email, then again with missing username and password|Expected: validation error returned. Actual: account created successfully with missing fields|High; allows incomplete accounts into the database|Fixed; verified via retest |
|BUG-03|  Signup succeeds with passwords outside the 8–14 character range, and with passwords containing only letters or only numbers (no mixed requirement enforced)  | Submit signup with a password under 8 chars, over 14 chars, all-letters, or all-numbers | Expected: rejected with a validation error. Actual: account created successfully regardless of length or composition | Medium (weak passwords allowed, but fucntionality not blocked) |Fixed; verified via retest |
|BUG-04 | No backend validation of email format; simple text was accepted as a valid email address when client-side attribute for type="email" was bypassed | Submit signup via curl with non-email format text string in the email input field | Expected: Error message for invalid email format. Actual: accepted and stored in database | Medium; data integrity issue, not a security vulnerablity | Open |

## Notes

- Status legend: ⬜ Not Run · ✅ Pass · ❌ Fail
- Update "Actual Result" and "Status" columns as each test case is run.
- Log any discovered bugs in the Bug Log table above, even if a related test case passes overall.
