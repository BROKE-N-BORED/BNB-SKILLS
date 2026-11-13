# Ship checklist

Work the gates in order. A gate that fails stops the shipment until it passes.

## 1. Zip modes

- [ ] Scripts stored as 0o100755, plain files as 0o100644, file type bits included
- [ ] Stored modes read back from the finished zip and confirmed
- [ ] Zip test-extracted to a fresh directory and the installer runs

Read stored modes back with:

```sh
python3 -c "import zipfile; z=zipfile.ZipFile('NAME.zip'); [print(i.filename, oct(i.external_attr>>16)) for i in z.infolist()]"
```

## 2. Fresh-unzip verification

- [ ] Full test suite green in the fresh unzip
- [ ] Own checks run in the fresh unzip
- [ ] Screenshots looked at, not just produced
- [ ] Icon and double-click installer present in the zip

## 3. Email (only when he explicitly asks for a zip email — otherwise skip)

- [ ] Filename and exact byte size recorded before sending
- [ ] Sent message read back: attachment name and size match the recorded values

## 4. Push

- [ ] No secrets in code: tree grepped for key patterns (below) — clean
- [ ] Secrets live only in gitignored files (.env, providers.json, key files), never in code
- [ ] User approval to push obtained
- [ ] Pushed files read back from GitHub and confirmed live

Grep the tree before pushing (immutable rule: sensitive information and APIs are NEVER in code):

```sh
grep -rnE "sk-[A-Za-z0-9]{8,}|ghp_[A-Za-z0-9]{8,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|xox[baprs]-[A-Za-z0-9-]+|hf_[A-Za-z0-9]{8,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|://[^/]+:[^/@]+@" --exclude-dir=.git --exclude-dir=__pycache__ . || true
```

A hit is a stop: move the value into a gitignored file and re-check. The only allowed key-shaped values are deliberate fake fixtures in tests, clearly commented as fake.

## 5. Release and hash-match

- [ ] Release cut with the zip attached
- [ ] Release asset downloaded back
- [ ] SHA-256 of the downloaded asset matches the local zip

```sh
sha256sum NAME.zip
```

## 6. Report

- [ ] Emailed filename and byte size reported (only when an email was sent)
- [ ] Pushed commit reported
- [ ] Live Release URL reported
- [ ] Hash-match confirmation reported
- [ ] Task receipt written (see [task-receipt-format](../../task-receipt-format/SKILL.md))
- [ ] Checks still needing the user's own PC named honestly
