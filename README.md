# 20 November 2026 — The World's News in One Image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Rzfr123/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Rzfr123/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper front page summing up Friday 20 November 2026. The masthead names the day; four panels plus four briefs cover the day's biggest stories.

Bounty: https://make.fun/bounty/news-image-20261120

## Stories

- **Peace talk in Shenzhen, then missiles over Kyiv** — Trump, Xi and Putin hold the first three-way talks and declare peace; hours later Russia fires 100+ missiles and 400 drones at Ukraine.
- **Russia's night barrage** — Bridges hit, power cut as cold bites; Poland scrambles jets.
- **Myanmar guilty of genocide** — The UN's top court rules 9–6: Myanmar bears state responsibility.
- **Anthropic up 34% on debut** — The first purely AI company to list publicly jumps on debut.
- **US–Venezuela military deal** — Ties restored months after the US captured Venezuela's president.
- Briefs: UK pledges 1,000+ drones for Ukraine in a £260m package; Trump pardons Pete Rose; Europe's E3 leaders call for a winter energy ceasefire; the US Senate rejects the Iran war-powers resolution 51–48.

## How it was made

`render.py` draws the front page programmatically with Pillow — no AI image generation, so every headline is exact. `main.ts` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and verifies its PNG magic bytes, IHDR dimensions (1024x1024), size and SHA-256 digest.

## Sources

- AP, CBS, CNN, The Times (Shenzhen summit; Russia's attack on Ukraine)
- CNN, AP (Kyiv barrage; Poland jets)
- AP, Le Monde (ICJ genocide verdict; Anthropic debut)
- BBC (Anthropic debut)
- AP (US–Venezuela deal)

## License

MIT — see LICENSE.
