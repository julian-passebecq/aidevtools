# Feature matrix — J Utility Palette

| Capability | Status | Notes |
| --- | --- | --- |
| Sidebar / Compact / Expanded layouts | Implemented | One shared application/data model |
| Normal window mode | Implemented | Standard Windows window |
| Always on top | Implemented | Native WPF `Topmost` behavior |
| Summon / hide | Implemented | Global mouse action reveals/hides app |
| Mouse 4 / Mouse 5 binding | Implemented | Action consumed while summon mode is active |
| Middle click / Ctrl + middle click | Implemented | Ctrl + middle click is the safer fallback |
| Hide on focus loss | Implemented | Optional summon preference |
| Open near cursor | Implemented | Clamped to working area of monitor under cursor |
| Temporary Keep open pin | Implemented | Does not change saved window mode |
| Project Clipboard | Implemented | Name + Repo + Site + optional Extra |
| Per-field copy flags | Implemented | Used by Copy Row / Copy All behavior |
| Explicit Open vs Copy | Implemented | Avoids ambiguous actions |
| Prompt modules | Implemented | Editable, enabled/disabled, ordered |
| Built-in project variables | Implemented | `{{project}}`, `{{repo}}`, `{{site}}`, `{{extra}}` |
| Recent prompt history | Implemented | Local history |
| Sticky notes | Implemented | Labels, pinned/archive state |
| Local JSON persistence | Implemented | Backup + import/export |
| Windows CI / smoke tests | Implemented | Package-free smoke test path |
| Archive filters | Next | Roadmap after V1 |
| Safer project editing validation | Next | Roadmap after V1 |
| Dynamic arbitrary prompt variables | Next | UI editors for custom placeholders |
| Persist per-view position/size | Next | Include off-screen recovery |
| Optional GitHub latest-commit status | Next | Manual refresh, no token in JSON |
| Self-contained Windows package | Next | Release packaging |
| Cloud synchronization | Out of scope | Explicit non-goal |
| Browser automation | Out of scope | Explicit non-goal |
| Rewrite PowerToys core | Out of scope | Explicit non-goal |
