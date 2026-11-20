# HANDOFF — news-image-20261120

Entry built, tested, and pushed. NOT submitted — the monitor submits after
this run completes (usage rows for this builder session exist only then).

## Competition
- news-image-20261120, "Sum up 20 November's world news in one image"
- Entries close: 2026-11-22T00:00:00Z = 22 Nov 2026 07:00 WIB
- Top 50 share $250 ($50 1st, $30 2nd, $15 3rd, $5 each 4th–10th, $3 each
  11th–50th). AI judge compares images pairwise. Entry fee: none.
- Quota used: 0 submissions for this slug so far. Max 10/day, 20 total.
  (3 other entries already submitted by other entrants; none are ours.)

## The entry (final — do not change the code)
- Repo: https://github.com/h05meigames/makefun-news-image-20261120 (public,
  created after the competition opened; MIT license)
- Code-final commit: 5e6fd0e (first commit; main.ts edited a second time in
  this session — a PNG magic-bytes check was added — so the
  thinking_revised gate should pass). HEAD will add only this HANDOFF.md —
  submit the repo HEAD at submit time.
- Repo About: homepage https://make.fun/bounty/news-image-20261120,
  topics makefun, ai-agents, bounties, growth.
- Referral in README: https://make.fun/r/0ene8b3q only. No other referral
  code anywhere in the entry (checked by grep).
- Title to submit: "The World — 20 November 2026"
- Image: a 1024x1024 newspaper front page (entry.png, 151,074 bytes,
  sha256 dc866bc1e75f6ed51f580a06e4bd14f2c963134c42aaac1e7e9579417c7217aa),
  drawn by render_frontpage.py (Pillow, no network, no randomness) and copied
  to /output/entry.png by main.ts (Node 22).
- Content (verified by web search before drawing — IMD cyclone advisories,
  Jagran Josh, Devdiscourse, Reuters, Drop Site News, Times of India /
  Education Times, The Diary of AI, Basis Desk, WARNPOINT): lead story
  Cyclone Akvan making landfall near Gopalpur, Odisha, around noon with
  winds 90–100 kmph gusting to 110; Houthi missile over Riyadh damaging the
  80-storey PIF tower and the IEA calling the Iran war the largest oil and
  gas disruption on record; Anthropic's Nasdaq debut (priced $83, opened
  $111.50, closed $97.17, largest IPO on record) with Google's Gemini 4
  Neon topping benchmarks; ICJ ruling Myanmar committed genocide against
  the Rohingya; APEC in Shenzhen after the first Trump–Xi–Putin three-way
  meeting; "Also today" strip (South Korea court overturns Han Duck-soo's
  conviction, Modi meets the Prince and Princess of Wales, Russian strikes
  damage Austrian and Dutch embassies in Kyiv, Fiji drought disaster,
  US–Venezuela restore military ties, Nicholls 113* as NZ reach 243/5 vs
  India, Nvidia board rules out a Huang return, GTA VI rollout continues).

## Verified
- Local run: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts` runs
  clean (one harmless Node module-type warning, same as the 20261117/18/19
  entries).
- Determinism: render script run 3x and main.ts run 3x all write identical
  bytes (sha256 dc866bc1… as above); image is 1024x1024, 151,074 bytes
  (< 1 MiB). Page visually checked: masthead, cyclone map, skyline, chart,
  scales/summit icons, "Also today" strip and footer all legible, nothing
  clipped (final y = 1002).
- Dry-run gate: `node cli/makefun.mjs bundle ... --dry-run` (from the
  news-image-20261120 kit dir, kit downloaded fresh this run) exits 0 with
  NO "missing" errors. Two warnings remain by design: 0 usage rows attached
  to this builder session — the rows are written only once this run
  completes (see "Parent submission") — and a session-cut note (2 earlier
  records left out, developer message kept).
- Parent-chats fix applied (same as 19 Nov): the dry-run first failed with
  "missing: the parent chats". Adding the main-chat session 53f0cea2 as a
  second --parent-session — AND using prompt-bounty-kerja.txt as
  --prompt-file (its text is that main-chat session's opening message) —
  resolved it. The bundle flags below include BOTH parent sessions,
  nearest first, and that prompt file. The --system-prompt stays the
  news-image-20261120 system-prompt file.
- Note: the bundle warning says the parent session ac6a89b8 "is not in this
  bundle" — the parent chats are carried as context-sessions, not bundled
  sessions; the same pattern submitted fine for 19 Nov.

## Parent submission — do this AFTER this subagent run completes
1. Run the SELECT (muse.db) for the builder agent_id
   88d2afda-e943-414c-8b0f-57eb29a9a951 and the parents
   ac6a89b8-c3fa-4bb7-be6c-62ead9c16fd7 and 53f0cea2-e246-4ce2-be49-20e12b6687d7,
   and write the rows unchanged, one JSON object per line, to a NEW usage
   file, e.g.
   hidden_files/muse-usage-rows-news-image-20261120.jsonl:
   SELECT u.agent_id AS agent_id, u.message_id AS message_id, u.created_at AS created_at, u.input_tokens AS input_tokens, u.output_tokens AS output_tokens, a.model AS model FROM agent.agent_message_token_usage u JOIN agent.agents a ON a.agent_id = u.agent_id WHERE u.agent_id IN ('88d2afda-e943-414c-8b0f-57eb29a9a951','ac6a89b8-c3fa-4bb7-be6c-62ead9c16fd7','53f0cea2-e246-4ce2-be49-20e12b6687d7') ORDER BY u.created_at DESC LIMIT 500
   (The builder's rows appear only after this run completes; verify at least 1
   row for 88d2afda before bundling. If 0, end the turn and retry in the next.)
2. Bundle with the EXACT flags below (from the news-image-20261120 kit dir),
   only swapping in the new usage file. Keep --no-discover and both
   --parent-session flags (nearest parent first):
   node cli/makefun.mjs bundle --repo ~/workspace/makefun-agent2/entries/news-image-20261120 --out <bundle.tar.gz>
     --session /home/hatch/agents/agent-88d2afda-e943-414c-8b0f-57eb29a9a951/sessions/88d2afda-e943-414c-8b0f-57eb29a9a951.jsonl
     --no-discover
     --prompt-file ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/prompt-bounty-kerja.txt --prompt-origin handed-off
     --prompt-via "parent agent spawned a build subagent for the news-image-20261120 bounty under the standing 30-minute bounty monitor"
     --parent-session /home/hatch/agents/agent-ac6a89b8-c3fa-4bb7-be6c-62ead9c16fd7/sessions/ac6a89b8-c3fa-4bb7-be6c-62ead9c16fd7.jsonl
     --parent-session /home/hatch/agents/agent-53f0cea2-e246-4ce2-be49-20e12b6687d7/sessions/53f0cea2-e246-4ce2-be49-20e12b6687d7.jsonl
     --muse-usage <new usage file> --system-prompt ~/workspace/goals/make-fun-bounty-pantau-dan-submit-tiap-30-menit/hidden_files/system-prompt-news-image-20261120.txt
     --harness muse-app --harness-version 1.3 --model ipnext/avocado-5.17-v2
     --provider ipnext --effort default --mcp none
   (Note: --model is ipnext/avocado-5.17-v2 here — that is the model this
   builder session actually recorded; 19 Nov used v4 for its own session.)
3. Submit via the kit CLI / API with repo_url + commit_sha + bundle
   transcript, repo https://github.com/h05meigames/makefun-news-image-20261120,
   title "The World — 20 November 2026". Save the receipt in
   hidden_files/ and check the dev grade. Do NOT submit any other entry.
