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

## 3. Email

- [ ] Filename and exact byte size recorded before sending
- [ ] Sent message read back: attachment name and size match the recorded values

## 4. Push

- [ ] User approval to push obtained
- [ ] Pushed files read back from GitHub and confirmed live

## 5. Release and hash-match

- [ ] Release cut with the zip attached
- [ ] Release asset downloaded back
- [ ] SHA-256 of the downloaded asset matches the local zip

```sh
sha256sum NAME.zip
```

## 6. Report

- [ ] Emailed filename and byte size reported
- [ ] Pushed commit reported
- [ ] Live Release URL reported
- [ ] Hash-match confirmation reported
- [ ] Task receipt written (see [task-receipt-format](../../task-receipt-format/SKILL.md))
- [ ] Checks still needing the user's own PC named honestly
