# Changelog

## v0.2.0

- Add explicit Session and Project handoff scopes, independent of local continuation or GitHub sharing.
- Add a project workflow covering goals, architecture, dependencies, capabilities and evidence, operations, prioritized backlog, permissions, and the first maintenance action.
- Follow the current request’s language for generated or edited handoff prose; explicit output-language instructions take precedence. Preserve commands, identifiers, paths, and original logs.
- Add a whole-project handoff example and update the bilingual homepage, documentation, scope comparison, and copyable prompts.
- Rename the repository to `xiaofengShi/handoff-skill`. The installed skill ID and `$session-handoff` invocation remain unchanged. Existing installations are not renamed.

The canonical website is now https://xiaofengshi.github.io/handoff-skill/ (Chinese: https://xiaofengshi.github.io/handoff-skill/zh/). Use the new Pages URL; repository URL redirects do not guarantee redirects for old Pages paths. Existing clones can update their remote with `git remote set-url origin https://github.com/xiaofengShi/handoff-skill.git`.

## v0.1.0

Initial MIT-licensed release with session continuation, GitHub-based sharing, a bilingual website, a Python installer, and a fixed-version runnable handoff example.
