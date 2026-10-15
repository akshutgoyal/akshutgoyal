<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=26&pause=1800&color=0969DA&center=true&vCenter=true&width=760&height=70&repeat=true&duration=3500&lines=Akshut+Goyal;I+build+local-first+Linux+tools;Systems+in+C+%C2%B7+on-device+ML+%C2%B7+blockchain;One+engine%2C+several+surfaces" alt="Akshut Goyal" />

**B.Tech @ Delhi Technological University · Delhi, India**

Local-first software, systems in C, and blockchain that actually solves something.

<p>
<a href="https://github.com/akshutgoyal"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
<a href="https://www.linkedin.com/in/akshut/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="https://akshutgoyal.github.io/"><img src="https://img.shields.io/badge/Portfolio-0969DA?style=flat-square&logo=githubpages&logoColor=white" alt="Portfolio" /></a>
<a href="mailto:akshutgoyal@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

<p>
<img src="https://komarev.com/ghpvc/?username=akshutgoyal&label=Profile%20views&color=0969da&style=flat-square" alt="Profile views" />
<img src="https://img.shields.io/github/followers/akshutgoyal?label=Followers&style=flat-square&color=0969da" alt="Followers" />
<img src="https://img.shields.io/badge/now%20building-the%20Aethel%20suite-8250DF?style=flat-square" alt="Now building: the Aethel suite" />
</p>

</div>

---

## 👋 About me

I like software that does one thing properly and then gets out of the way. Most of what I build is **local-first**: your data lives on your machine, one engine does the real work, and whichever surface you actually want — a terminal, a GTK window, a browser tab — sits on top of that same engine.

I'm not precious about polish before the core works, and I'm honest about what isn't finished yet.

- 🖥️ **Linux-native desktop** — GTK4/libadwaita, Qt/PySide6, systemd user units, Arch packaging
- 🔐 **Systems & security** — C, process confinement with `bwrap`/Seatbelt, permissions that fail closed
- ⛓️ **Blockchain, when it earns its place** — soulbound records, consent expressed as contract state rather than policy
- 🤖 **On-device ML** — YOLOv8 → ONNX → TFLite, so inference runs on the phone instead of a datacenter
- 🌐 **Where it started** — static sites and PHP/Laravel apps from 2022, which is why I still reach for a plain HTML file when that's the honest answer
- 📚 **Learning in the open** — working through a self-written CS curriculum, fundamentals to systems

---

## 📌 Featured projects

| Project | What it does | Built with |
| :--- | :--- | :--- |
| 🌱 **[ROADSENSE](https://github.com/akshutgoyal/ROADSENSE)** | Gives street defects a site history and an accountable fix — potholes detected on-device, C&D heaps captured by hand, both landing in one engineer worklist with closure audit and recycler routing. | Flutter · PyTorch / YOLOv8 · React 19 · MapLibre · AWS |
| 🩺 **[ApnaRecord](https://github.com/akshutgoyal/ApnaRecord)** | Patient-owned medical records. Login is a wallet, a record is a soulbound token, permission is a smart contract — verifiable by anyone, for free, without trusting the operator. | Solidity · OpenZeppelin · Base Sepolia · React · Express · Cloudflare R2 |
| ⛓️ **[AarogyaChain](https://github.com/akshutgoyal/aarogyachain)** · **[website](https://github.com/akshutgoyal/aarogyachain-website)** | The contract-first predecessor to ApnaRecord: consent as chain state, with a production-look React demo UI ([live build](https://akshutgoyal.github.io/aarogyachain-website/)) and an advisory-only AI summariser that never touches the chain or a key. | Solidity · React · Vite · ethers v6 · MetaMask |
| 🎓 **[aethel-vmc-injector](https://github.com/akshutgoyal/aethel-vmc-injector)** · **[extension](https://github.com/akshutgoyal/aethel-vmc-extension)** | Turns a coaching-portal roll number and activation code into a browser session — a CLI/Node injector plus an unpacked MV3 Chrome extension that signs the active tab in. | TypeScript · Node · Chrome MV3 |
| 🐍 **[zulip-processor-practice](https://github.com/akshutgoyal/zulip-processor-practice)** | Working through the Zulip API surface against a real server to practise reading and extending someone else's codebase. | Python · Zulip API |
| ⚙️ **[CS101](https://github.com/akshutgoyal/CS101)** · **[SSE-Task-1](https://github.com/akshutgoyal/SSE-Task-1)** · **[Keylogger](https://github.com/akshutgoyal/Keylogger)** | C fundamentals, from pointers and structs up to a Linux key-event reader built as a step-by-step exercise for DTU's EHAX cybersecurity club. | C · Make |

---

## 🚀 What I'm building

### 🧩 The Aethel suite — 16 repositories

One idea applied a lot of times: **local-first Linux tools** where your data stays on your machine. Most of it is private while it's still in the shop, but the shape is consistent enough to be worth naming.

- **`aethel-launcher`** — a multi-slot cloud-gaming session launcher. A single Playwright engine sits behind **four front-ends** (GTK4/libadwaita, a FastAPI web dashboard, a CLI, and PySide6), and one supervision lock makes sure only one process ever gets to start or stop anything. No licence key, no telemetry, no phone-home.
- **`aethel-todo`** — a local-first task and chore manager. A Bun daemon owns SQLite and the recurrence engine; the CLI, an Ink TUI streamed over SSE, and an installable React PWA are just surfaces in front of it. Gamified on purpose — points ledgers, per-task streaks, and a rewards catalogue you redeem against yourself.
- **`aethel-harness`** — a plugin-first AI agent harness. The append-only session log is the only real source of truth; model history is *derived* from it, never stored twice. Permissions fail closed, and every registration hands back a disposer that unwinds in reverse.
- A dozen smaller Linux utilities around them: `studio`, `janitor`, `receipts`, `restock`, `surveyor`, `macro`, `reddit-finder`, `comment-manager`, `description-manager`, `game-launcher`, `adventures`.

**Public from the suite:** the **[VMC session injector](https://github.com/akshutgoyal/aethel-vmc-injector)** and its **[Chrome extension](https://github.com/akshutgoyal/aethel-vmc-extension)**.

### 🌱 RoadSense — street defects with a site history

Built for WeMakeDevs *Environmental Hacks*. It turns a walk into a road survey: potholes get detected on-device and geotagged automatically, C&D heaps are photographed by hand, and both end up in the same engineer worklist with evidence, a closure audit, and recycler routing. Nearby sightings merge into persistent site records, so a dump that keeps coming back reopens the same case instead of arriving as yet another new complaint.

### 🩺 Patient-owned medical records

**[ApnaRecord](https://github.com/akshutgoyal/ApnaRecord)** and its predecessor **[AarogyaChain](https://github.com/akshutgoyal/aarogyachain)** are two attempts at the same question — what if the patient held the record instead of the hospital? Login is a wallet, a record is a soulbound token, and permission is a smart contract that re-checks on every call. Anyone can verify a record for free, without trusting whoever is running the thing.

---

## 🛠️ Tech I work in

**Languages**

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" />
<img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black" />
<img src="https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" />
</p>

**Frontend & Desktop**

<p>
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" />
<img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" />
<img src="https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white" />
<img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" />
<img src="https://img.shields.io/badge/GTK4_%2F_libadwaita-4A86CF?style=flat-square&logo=gtk&logoColor=white" />
<img src="https://img.shields.io/badge/Qt_%2F_PySide6-41CD52?style=flat-square&logo=qt&logoColor=black" />
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/jQuery-0769AD?style=flat-square&logo=jquery&logoColor=white" />
</p>

**Backend & Data**

<p>
<img src="https://img.shields.io/badge/Bun-000000?style=flat-square&logo=bun&logoColor=white" />
<img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=nodedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
<img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" />
<img src="https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white" />
<img src="https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white" />
<img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" />
<img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black" />
</p>

**Blockchain**

<p>
<img src="https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white" />
<img src="https://img.shields.io/badge/Ethereum-3C3C3D?style=flat-square&logo=ethereum&logoColor=white" />
<img src="https://img.shields.io/badge/ethers.js-2535A0?style=flat-square&logo=ethers&logoColor=white" />
<img src="https://img.shields.io/badge/OpenZeppelin-4E5EE4?style=flat-square&logo=openzeppelin&logoColor=white" />
<img src="https://img.shields.io/badge/Base_Sepolia-0052FF?style=flat-square&logo=coinbase&logoColor=white" />
</p>

**ML & Automation**

<p>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" />
<img src="https://img.shields.io/badge/Ultralytics_YOLOv8-111F68?style=flat-square&logo=yolo&logoColor=white" />
<img src="https://img.shields.io/badge/ONNX-005CED?style=flat-square&logo=onnx&logoColor=white" />
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" />
<img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" />
<img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" />
</p>

**Platform & Tooling**

<p>
<img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" />
<img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=flat-square&logo=archlinux&logoColor=white" />
<img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white" />
<img src="https://img.shields.io/badge/Cloudflare_R2-F38020?style=flat-square&logo=cloudflare&logoColor=white" />
</p>

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

I'm always happy to talk about local-first design, Linux tooling, on-device ML, or why a smart contract is the right answer to a question you haven't asked yet.

<p>
<a href="https://www.linkedin.com/in/akshut/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:akshutgoyal@gmail.com"><img src="https://img.shields.io/badge/Say_hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<a href="https://github.com/akshutgoyal?tab=followers"><img src="https://img.shields.io/badge/Follow-181717?style=for-the-badge&logo=github&logoColor=white" alt="Follow" /></a>
</p>

<br/>

<sub>Most of the interesting work is in private repos — it ships when it's honest about what isn't finished.</sub>

</div>
