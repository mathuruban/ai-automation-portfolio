# 4 · Agentic job-search operations (in use)

**Problem.** A job search across many portals (Workday, SuccessFactors, JOIN, LinkedIn Easy Apply, company forms) is repetitive, but every submission is consequential and must be accurate.

## Setup

- **Browser agent** (Claude driving Chrome) finds roles, reads each full description and screens them on hard requirements first: language level, years of experience, degree, location, salary floor.
- **Every exclusion is recorded with its reason**, so a role is never screened twice. Before any application, the agent checks the tracker and earlier receipts for **duplicates**. In one case that check stopped a second application to a role that had been submitted about a week earlier.
- **Tailoring from a fact base.** CVs and cover letters are generated from verified facts only (HTML → headless PDF). Claims that couldn't be verified are removed before rendering.
- **Human approval at the right points:**
  - The agent asks before each submission, and for every salary figure or legal-terms checkbox.
  - Logins and 2FA always stay with the human.
  - The agent refuses to write answers on forms that forbid AI-written text.
- **Daily scheduled run** repeats the search and drafts applications for approval.

## Lessons

- **Most of the value is in screening, not writing.** Most roles fail on one hard requirement. Finding that early saves far more time than a polished letter.
- **Portals break in predictable ways:**
  - React inputs that ignore synthetic typing.
  - Hidden file inputs.
  - Sessions that expire mid-form.
  - Profile data that silently overrides the uploaded CV.

  Each needed a specific, reusable technique.
- **Status words matter.** Only an on-screen or email confirmation counts as "submitted". Anything else is "prepared".

*Operated by me with AI agents. Personal data and employer details are not published here.*
