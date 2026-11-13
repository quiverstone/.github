<div align="center">

# 🏹 Quiverstone

<a href="https://www.quiverstone.io"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=22&pause=1200&color=FF9900&center=true&vCenter=true&width=600&height=50&lines=Jump+into+every+client+AWS+Organization;Client+%E2%86%92+Org+%E2%86%92+Account+inventory;Temporary+STS+access+%E2%80%A2+no+stored+keys;AWS+consulting+%26+managed+services" alt="Jump into every client AWS Organization · Client → Org → Account inventory · Temporary STS access, no stored keys · AWS consulting & managed services" /></a>

**The single pane of glass for AWS multi-account chaos — built for MSPs, AWS consultants, and the teams behind them.**

[![Website](https://img.shields.io/badge/quiverstone.io-232F3E?style=for-the-badge&logo=googlechrome&logoColor=FF9900)](https://www.quiverstone.io)
[![Start free](https://img.shields.io/badge/Start_free-FF9900?style=for-the-badge&logo=amazonwebservices&logoColor=232F3E)](https://app.quiverstone.io/auth/sign-up)
[![Docs](https://img.shields.io/badge/Docs-0d1117?style=for-the-badge&logo=readthedocs&logoColor=FF9900)](https://docs.quiverstone.io/)
[![Book a demo](https://img.shields.io/badge/Book_a_demo-0d1117?style=for-the-badge&logo=googlecalendar&logoColor=FF9900)](https://meet.quiverstone.io/demo)
<br/>
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/company/quiverstone)
[![X](https://img.shields.io/badge/@quiverstoneio-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/quiverstoneio)
[![Newsletter](https://img.shields.io/badge/ArroWS_%26_Mortar-FF9900?style=for-the-badge&logo=substack&logoColor=232F3E)](https://newsletter.quiverstone.io/)
[![Community](https://img.shields.io/badge/Community-232F3E?style=for-the-badge&logo=discourse&logoColor=FF9900)](https://community.quiverstone.io/)

</div>

Most AWS tooling assumes you manage one giant organization. Quiverstone is for the rest of us —
dozens of clients, a portfolio of unrelated AWS Organizations, standalone accounts on the side,
and zero appetite for losing security posture every time you switch between them.

### ⚡ What Quiverstone does

| | |
| --- | --- |
| 🗂️ **Inventory** | Client → Org → Account in one place. Enroll an Organization once and member accounts are discovered automatically; standalones sit beside them. |
| 🔐 **Access** | Temporary STS role assumption with External ID — direct or chained — straight from your browser. Your browser session, their CloudTrail. |
| 🔎 **Discover** | Search resources and core settings across accounts and customer organizations. |
| 🧰 **Utilities** | A shared quiver of tools, references, and deployment templates so every operator follows the same process. |
| 💼 **Practice economics** | Track Customer, Org, Project, and engagement type (Resale, Managed Services, Professional Services) to keep work billable. |

> [!NOTE]
> **We never store long-term client credentials.** Access is an IAM role with a trust policy and External ID —
> deploy a Quiverstone-managed role via CloudFormation / StackSets or reuse one you already have.
> Team access is scoped by **Group × Account × Role**. More on [how access works →](https://www.quiverstone.io/access/)

### 🛠️ AWS consulting & managed services

The people who built Quiverstone run AWS for clients — one account or a portfolio of client Organizations.

- **Consulting & advisory** — architecture reviews, Organizations / Control Tower strategy, security, IAM, cost, and AI on AWS
- **Projects** — assessments, landing zones, governance & guardrails, migrations, infrastructure as code
- **Managed AWS** — monitoring, patching, backup oversight, access hygiene, findings triage, and cost reviews

Past work includes U.S. Navy, Air Force, and Space Force contract support, DOI/USGS cloud operations,
GovCloud and FedRAMP environments, and commercial teams in healthcare, logistics, and local government.
**[Explore services →](https://www.quiverstone.io/professional-services/)**

### 📦 Open source

Free, public building blocks — the same templates we use with customers and in our blog posts.

| Repository | What it is |
| --- | --- |
| [**armory**](https://github.com/quiverstone/armory) | Ready-to-use CloudFormation templates, SCPs/RCPs, and scripts for AWS foundations — IAM, Organizations, Config, Control Tower, VPC, billing, and more. |
| [**assets**](https://github.com/quiverstone/assets) | The Quiverstone **role catalog**: Inventory and Access roles for Browser Session, Direct, and Chained access, for single accounts or org-wide via StackSets. |
| [**docs**](https://github.com/quiverstone/docs) | Source for [docs.quiverstone.io](https://docs.quiverstone.io). Spot a gap? PRs welcome. |

### 🧰 Built with

<p>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900" alt="AWS" />
  <img src="https://img.shields.io/badge/Organizations_%26_STS-232F3E?style=flat-square&logo=amazoniam&logoColor=FF9900" alt="AWS Organizations & STS" />
  <img src="https://img.shields.io/badge/CloudFormation-FF4F8B?style=flat-square&logo=amazonwebservices&logoColor=white" alt="CloudFormation" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

### 📝 From the blog

<!-- BLOG-POST-LIST:START -->
- [Automating Contact Updates Across Accounts In Your Organization](https://www.quiverstone.io/blog/automating-contact-updates-across-accounts-in-your-organization/) <sub>Jan 2026</sub>
- [Scaling Performance Testing: Leveraging the AWS Distributed Load Testing Solution](https://www.quiverstone.io/blog/scaling-performance-testing-leveraging-the-aws-distributed-load-testing-solution/) <sub>Jan 2026</sub>
- [Quiverstone: The Single Pane of Glass for AWS Multi-Account Chaos](https://www.quiverstone.io/blog/quiverstone-the-single-pane-of-glass-for-aws-multi-account-chaos/) <sub>Jan 2026</sub>
<!-- BLOG-POST-LIST:END -->

**[All posts →](https://www.quiverstone.io/blog/)** · Get it in your inbox with **[ArroWS & Mortar](https://newsletter.quiverstone.io/)**, our free AWS management & governance newsletter.

### 💬 Get help

| Need | Go to |
| --- | --- |
| Product docs | [docs.quiverstone.io](https://docs.quiverstone.io/) |
| Support | [support.quiverstone.io](https://support.quiverstone.io/) |
| Feature requests & changelog | [quiverstone.canny.io](https://quiverstone.canny.io/changelog) |
| Security reports | [Security policy](https://github.com/quiverstone/.github/blob/main/SECURITY.md) |
| Talk to us | [Contact](https://www.quiverstone.io/contact/) · [Book 20 min](https://meet.quiverstone.io/demo) |

<div align="center">
<sub><i>Governance shouldn't be a barrier to innovation — it should be the foundation that enables it.</i></sub>
</div>
