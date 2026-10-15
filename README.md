<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=32&pause=1200&color=0969DA&center=true&vCenter=true&width=800&height=70&lines=Akshut+Goyal;I+build+local-first+tools;One+engine%2C+several+surfaces;Python+%C2%B7+TypeScript+%C2%B7+Solidity+%C2%B7+C" alt="Akshut Goyal" />

**B.Tech @ Delhi Technological University · Delhi, India**

Local-first software, systems in C, and blockchain that actually solves something.

<a href="https://github.com/akshutgoyal"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
<a href="https://akshutgoyal.github.io/"><img src="https://img.shields.io/badge/Portfolio-0969DA?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
<a href="mailto:akshutgoyal@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

<img src="https://komarev.com/ghpvc/?username=akshutgoyal&label=Profile%20views&color=0969da&style=flat" alt="Profile views" />
<img src="https://img.shields.io/github/followers/akshutgoyal?label=Followers&style=flat&color=0969da" alt="Followers" />

</div>

---

## 👋 About me

I build software the way I wish more of it were built: **local-first**, honest about which parts are finished, and quiet about the rest. Most of what I make follows one pattern — put the real work in a single engine, then let whichever surface you actually want (a terminal, a GTK window, a browser) drive that same engine.

- 🖥️ **Linux-native desktop** — GTK4/libadwaita, Qt/PySide6, systemd user units, Arch packaging
- 🔐 **Systems & security** — C, process confinement with `bwrap`/Seatbelt, fail-closed permission design
- ⛓️ **Blockchain that earns its place** — soulbound records, consent expressed as contract state rather than policy
- 🤖 **On-device ML** — YOLOv8 → ONNX → TFLite, so inference runs on the phone instead of a datacenter
- 🌐 **Where it started** — static sites and PHP/Laravel apps from 2022, which is why I still reach for a plain HTML file when that's the honest answer
- 📚 **Learning in the open** — currently working through a self-written CS curriculum from fundamentals to systems

---

## 🚀 What I'm building

### 🧩 The Aethel suite — 16 repositories

One idea applied repeatedly, most of it private while it's still in the shop. Every piece is a **local-first Linux tool**: your data stays on your machine, one engine runs the show, and several interfaces front it.

- **`aethel-launcher`** — a multi-slot cloud-gaming session launcher. One Playwright engine behind **four front-ends** (GTK4/libadwaita, a FastAPI web dashboard, a CLI, and PySide6), a single supervision lock so only one process starts or stops anything. No licence key, no telemetry, no phone-home.
- **`aethel-todo`** — a local-first task and chore manager. A Bun daemon owns SQLite and the recurrence engine; a CLI, an Ink TUI streamed over SSE, and an installable React PWA are the surfaces. Gamified on purpose: points ledgers, per-task streaks, a rewards catalogue you redeem against yourself.
- **`aethel-harness`** — a plugin-first AI agent harness. The append-only session log is the only source of truth (model history is *derived*, never stored), permissions fail closed, and every registration returns a disposer that unwinds in reverse.
- A dozen smaller Linux utilities around them: `studio`, `janitor`, `receipts`, `restock`, `surveyor`, `macro`, `reddit-finder`, `comment-manager`, `description-manager`, `game-launcher`, `adventures`.

**Public from the suite:** the **[VMC session injector](https://github.com/akshutgoyal/aethel-vmc-injector)** and its **[Chrome extension](https://github.com/akshutgoyal/aethel-vmc-extension)**.

### 🌱 RoadSense — street defects with a site history

Built for WeMakeDevs *Environmental Hacks*. Turns a walk into a road survey: potholes detected on-device and geotagged automatically, C&D heaps photographed by hand, and both reaching the same engineer worklist with evidence, closure audit and recycler routing. Nearby sightings merge into persistent site records, so a recurring dump reopens the same case instead of arriving as a new complaint.

### 🩺 Patient-owned medical records

**[ApnaRecord](https://github.com/akshutgoyal/ApnaRecord)** and its predecessor **[AarogyaChain](https://github.com/akshutgoyal/aarogyachain)** ask the same question twice: what if the patient held the record instead of the hospital? Login is a wallet, a record is a soulbound token, permission is a smart contract that re-checks every call — and anyone can verify a record for free, without trusting the operator.

---

## 🛠️ Tech I work in

**Languages**

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black" />
<img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white" />
<img src="https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" />
</p>

**Frontend & Desktop**

<p>
<img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
<img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
<img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white" />
<img src="https://img.shields.io/badge/GTK4_%2F_libadwaita-4A86CF?style=for-the-badge&logo=gtk&logoColor=white" />
<img src="https://img.shields.io/badge/Qt_%2F_PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=black" />
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white" />
</p>

**Backend & Data**

<p>
<img src="https://img.shields.io/badge/Bun-000000?style=for-the-badge&logo=bun&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" />
<img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white" />
<img src="https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" />
</p>

**Blockchain**

<p>
<img src="https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white" />
<img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white" />
<img src="https://img.shields.io/badge/ethers.js-2535A0?style=for-the-badge&logo=ethers&logoColor=white" />
<img src="https://img.shields.io/badge/OpenZeppelin-4E5EE4?style=for-the-badge&logo=openzeppelin&logoColor=white" />
<img src="https://img.shields.io/badge/Base_Sepolia-0052FF?style=for-the-badge&logo=coinbase&logoColor=white" />
</p>

**ML & Automation**

<p>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/Ultralytics_YOLOv8-111F68?style=for-the-badge&logo=yolo&logoColor=white" />
<img src="https://img.shields.io/badge/ONNX-005CED?style=for-the-badge&logo=onnx&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white" />
<img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
</p>

**Platform & Tooling**

<p>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=archlinux&logoColor=white" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white" />
<img src="https://img.shields.io/badge/Cloudflare_R2-F38020?style=for-the-badge&logo=cloudflare&logoColor=white" />
</p>

---

## 📌 Featured projects

| Project | What it does | Built with |
| :--- | :--- | :--- |
| 🌱 **[ROADSENSE](https://github.com/akshutgoyal/ROADSENSE)** | Gives street defects a site history, an accountable fix and a path to reuse — potholes detected on-device, C&D heaps captured by hand, both landing in one engineer worklist with closure audit and recycler routing. | Flutter · PyTorch / YOLOv8 · React 19 · MapLibre · AWS |
| 🩺 **[ApnaRecord](https://github.com/akshutgoyal/ApnaRecord)** | Patient-owned medical records. Login is a wallet, a record is a soulbound token, permission is a smart contract — verifiable by anyone, for free, without trusting the operator. | Solidity · OpenZeppelin · Base Sepolia · React · Express · Cloudflare R2 |
| ⛓️ **[AarogyaChain](https://github.com/akshutgoyal/aarogyachain)** · **[website](https://github.com/akshutgoyal/aarogyachain-website)** | The contract-first predecessor to ApnaRecord: consent as chain state, with a production-look React demo UI ([live build](https://akshutgoyal.github.io/aarogyachain-website/)) and an advisory-only AI summariser that never touches the chain or a key. | Solidity · React · Vite · ethers v6 · MetaMask |
| 🎓 **[aethel-vmc-injector](https://github.com/akshutgoyal/aethel-vmc-injector)** · **[extension](https://github.com/akshutgoyal/aethel-vmc-extension)** | Turns a coaching-portal roll number and activation code into a browser session — a CLI/Node injector plus an unpacked MV3 Chrome extension that signs the active tab in. | TypeScript · Node · Chrome MV3 |
| 🐍 **[zulip-processor-practice](https://github.com/akshutgoyal/zulip-processor-practice)** | Working through the Zulip API surface against a real server to practise reading and extending someone else's codebase. | Python · Zulip API |
| ⚙️ **[CS101](https://github.com/akshutgoyal/CS101)** · **[SSE-Task-1](https://github.com/akshutgoyal/SSE-Task-1)** · **[Keylogger](https://github.com/akshutgoyal/Keylogger)** | C fundamentals, from pointers and structs up to a Linux key-event reader built as a step-by-step exercise for DTU's EHAX cybersecurity club. | C · Make |

---

## 🗄️ Also public

The rest of what's up here — earlier web work and a couple of automation tools, newest first.

| Project | What it is | Built with |
| :--- | :--- | :--- |
| 🎯 **[Earnpt-Automation](https://github.com/akshutgoyal/Earnpt-Automation)** | Playwright driving an already-signed-in Chrome profile over the DevTools Protocol — opens AI tabs, sends prompts, and steps through accounts behind a verified-view counter. | JavaScript · Playwright · CDP |
| 🛡️ **[DDOS-Tester](https://github.com/akshutgoyal/DDOS-Tester)** | An async load tester that ramps concurrency gradually to find where a server's rate limits and breaking points actually sit. Carries an explicit authorised-use disclaimer. | Python · aiohttp |
| 💚 **[Green-Pulse-Connect](https://github.com/akshutgoyal/Green-Pulse-Connect)** | A sustainability community platform — green living tips, renewable energy, zero-waste living, eco-product reviews and climate advocacy in one place. | Laravel 10 · PHP 8.1 · Livewire · MySQL |
| ♾️ **[SrinivasaRamanujan](https://github.com/akshutgoyal/SrinivasaRamanujan)** · **[Independia](https://github.com/akshutgoyal/Independia)** | Two Design Championship entries — a tribute to Ramanujan (2023) and a journey-towards-independence piece (2022). Both still have live builds. | HTML · CSS · JavaScript |
| ✍️ **[Bloggers-Hub](https://github.com/akshutgoyal/Bloggers-Hub)** | A multi-page blog site — about, contact, privacy, terms and a working registration flow — written before I ever reached for a framework. | HTML · CSS · Bootstrap · jQuery |
| 🏛️ **[Virtual-Museum](https://github.com/akshutgoyal/Virtual-Museum)** | A PHP virtual tour of the National Museum, New Delhi, with a self-hosted carousel and a downloadable brochure. | PHP · jQuery · Owl Carousel |
| 📈 **[GrowtheX](https://github.com/akshutgoyal/GrowtheX)** | A landing site for a stock-trading concept, complete with an animated profit calculator in the marketing copy. | HTML · CSS · jQuery · Lottie |

---

## 🐍 Contribution graph

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/akshutgoyal/akshutgoyal/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/akshutgoyal/akshutgoyal/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/akshutgoyal/akshutgoyal/output/github-contribution-grid-snake.svg" />
</picture>

</div>

---

## 🤝 Connect

<div align="center">

I'm happy to talk about local-first design, Linux tooling, on-device ML, or why a smart contract is the right answer to a question you haven't asked yet.

<a href="mailto:akshutgoyal@gmail.com"><img src="https://img.shields.io/badge/Say_hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<a href="https://github.com/akshutgoyal?tab=followers"><img src="https://img.shields.io/badge/Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="Follow" /></a>

<br/><br/>

<sub>Most of the interesting work is in private repos — it ships when it's honest about what isn't finished.</sub>

</div>
