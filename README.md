# robot-executable

This repo demonstrates how to make an executable from a Robot Framework project.

0. (use virtualenv)
1. `pip install ./python`
2. `cd python; pyinstaller run.spec`
3. Have fun times running the resulting `python/dist/run/run.exe`

## TODO (Get rid of these things)

- No single-executable. Single-exe in pyinstaller works by extracting contents to
  a temporary folder, and using resources (.robot files, the HTML report template)
  from that folder would require some extra effort.
- When running run.exe, the current working dir should be the same as
  run.exe location.