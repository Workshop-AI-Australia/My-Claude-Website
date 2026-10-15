"""Content for the Workshop AI fact sheet and Q&A page.

Edit facts and answers here, then run:  python3 _src/build.py
That regenerates facts/index.html, ai-for-tradies/index.html, sitemap.xml,
llms.txt and the structured data block in index.html, so the visible page and
the structured data never drift apart.

Rules for anything in this file:
- Australian spelling, no em dashes.
- No figure without a source we have read. No invented client results.
- Answer first, in the first sentence. Detail after.
"""

SITE = "https://workshopai.com.au"
UPDATED = "2026-10-14"            # ISO date, shown on both pages and in sitemap
UPDATED_HUMAN = "14 October 2026"
GA_ID = "G-SB01RKTVMZ"           # Google Analytics 4, property "Workshop AI"

ORG = {
    "name": "Workshop AI",
    "legal_name": "Workshop AI Pty Ltd",
    "abn": "63 698 704 915",
    "abn_url": "https://abr.business.gov.au/ABN/View?abn=63698704915",
    "founded": "2026",
    "founder": "Justin Watts",
    "email": "info@workshopai.com.au",
    "phone_display": "0431 254 769",
    "phone_intl": "+61431254769",
    "booking_url": "https://calendar.app.google/vLCXuaZViuscaWe96",
    "postcode": "3015",
    "base": "Hobsons Bay, in Melbourne's western suburbs, Victoria",
    "suburbs": ["Altona", "Williamstown", "Newport", "Laverton", "Point Cook",
                "Werribee", "Footscray", "Sunshine", "Brooklyn", "Derrimut",
                "Truganina"],
    "one_liner": ("Workshop AI is a Melbourne-based AI implementation consultancy "
                  "that helps Australian tradies and trade, service and industrial "
                  "businesses put AI to work in the office, with fixed prices and "
                  "hands-on delivery."),
    "description": ("Workshop AI helps Australian tradies and trade and service "
                    "businesses put AI to work: HVAC, plumbing, electrical, "
                    "construction and logistics. It sets up AI tools such as Claude "
                    "safely for owners and teams, maps how the business runs, and "
                    "builds custom AI agents and automations into the systems the "
                    "business already uses. Based in Hobsons Bay in Melbourne's west, "
                    "in person across Melbourne and remote Australia-wide. Fixed "
                    "prices from A$1,500."),
}

INDUSTRIES = [
    "HVAC and refrigeration",
    "Plumbing and gas",
    "Electrical",
    "Construction and building",
    "Logistics and transport",
    "Drafting and surveying",
    "Hospitality and other service businesses",
]

TOOLS = ["Claude", "Simpro", "ServiceM8", "AroFlo", "Tradify", "Fergus",
         "Buildxact", "Xero", "MYOB", "HubSpot", "Microsoft 365 and Outlook",
         "Google Workspace and Gmail", "Excel"]

# (name, price, price_number_for_schema, unit_note, summary)
SERVICES = [
    ("Claude for Owners", "A$1,500", 1500, "Two one-on-one video sessions",
     "AI set up on the owner's desk first: Claude connected to files, email and "
     "calendar, a company-wide Claude Project with the business's context, and a "
     "one-page guide to using it safely with client information. Credited in full "
     "if the business goes further within 60 days."),
    ("Claude for Business", "A$2,500", 2500, "Set up and running within a week",
     "The team on Claude properly: set up for nominated staff, connected to everyday "
     "tools, a shared company-wide Claude Project, AI standards and governance, a "
     "team intro session and a follow-up two weeks later. Credited in full towards "
     "Discovery within 60 days."),
    ("Discovery", "A$3,600", 3600, "Four stages, about a month",
     "A complete picture of how the business really works before any tool is "
     "recommended: AI standards and governance, a written AI use policy, a systems "
     "audit and confidential team survey, a workflow map, a scored AI Opportunity "
     "Map, and a findings report with a recommended pathway."),
    ("Custom Builds", "From A$4,400 a month", 4400, "Monthly retainer or fixed-price project",
     "Custom AI agents and automations built into the job, file and accounting "
     "systems the business already runs, one defined piece at a time with a clear "
     "definition of done. Month to month, no lock-in."),
    ("Document Standard", "A$2,000 as an add-on, A$2,750 on its own", 2000, "Two weeks",
     "Up to four client-facing documents (quotes, reports, letters) built into Claude "
     "in the business's own format, wording and branding, with two rounds of "
     "revisions. A$2,000 as an add-on or A$2,750 on its own; A$4,000 for Claude for "
     "Business and Document Standard booked together."),
]

LEVELS = [
    ("Configure", "The right tools in place, used safely and the same way by everyone."),
    ("Connect", "The tools join up with the software the business already runs, so "
                "the business comes out of people's heads into one picture."),
    ("Know", "The business gains one place to ask about its own goals and "
             "performance, and starts getting direction, not just reports."),
    ("Act", "Bounded AI agents take defined work off people's plates, each doing "
            "one job, on rails."),
    ("Learn", "The system learns from its own record and keeps everything below it "
              "working as the business changes."),
]

# Justin's own words (Oct 2026), lightly edited into the third person.
JUSTIN_BIO = (
    "Justin Watts is a Director of Workshop AI. He helps trades and small businesses "
    "work smarter, finding where AI can take the manual grind off people's plates (the "
    "quotes, the double entry, the same questions answered over and over) and freeing "
    "them up for higher-value, more meaningful work. He has spent more than 15 years "
    "building the systems that growing businesses run on, and the last few applying AI "
    "across them, in property tech, finance, health and social enterprise. Whatever the "
    "industry or the technology, his approach stays the same: audit how things work now, "
    "find the manual steps, design something better, and build it."
)

# ---------------------------------------------------------------------------
# Sources we have read and cite on the Q&A page
SRC = {
    "abs": "https://www.abs.gov.au/media-centre/media-releases/business-adoption-artificial-intelligence-accelerates-2024-25",
    "oaic_ai": "https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products",
    "oaic_sb": "https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/small-business",
    "fwo": "https://www.fairwork.gov.au/tools-and-resources/best-practice-guides/consultation-and-cooperation-in-the-workplace",
    "acma": "https://www.acma.gov.au/avoid-sending-spam",
    "asbas": "https://business.gov.au/expertise-and-advice/digital-solutions-australian-small-business-advisory-services",
}


def a(key, text):
    return f'<a href="{SRC[key]}" rel="noopener" target="_blank">{text}</a>'


# ---------------------------------------------------------------------------
# Q&A. Each theme: (slug, title, [(id, question, answer_html), ...])
THEMES = [
("getting-started", "Getting started", [
("where-to-start",
 "Where should a tradie start with AI?",
 """<p>Start with the admin job that eats the most office hours and follows the same steps every time, usually reading emails, entering jobs, writing quotes or chasing invoices. Don't start with the flashiest tool.</p>
<p>Write down the three most repetitive admin jobs in your week, how long each takes and who does it. The one with the most hours and the clearest rules is your first project. Fix that end to end, check it saves real time, then move to the next. That's how Workshop AI works with trade businesses: one real problem solved before anything bigger is on the table.</p>"""),

("what-can-ai-do",
 "What can AI actually do in a trade business today?",
 """<p>AI is reliably good at reading and writing: pulling details out of emails and work orders, drafting quotes and reports, summarising job notes, answering questions about your own documents and filling in forms.</p>
<ul><li>Reading work orders, supplier quotes and customer emails, and putting the details into your job system</li>
<li>Turning site notes, photos or a voice memo into a quote description</li>
<li>Drafting customer emails, follow-ups and invoice reminders in your voice</li>
<li>Producing branded reports and documents in a consistent format</li>
<li>Finding information buried in job folders, drawings and contracts</li>
<li>Answering the phone or texting back when you can't pick up</li></ul>
<p>It's weaker at pricing without your rates, judgement calls it can't check, and anything where a mistake is costly and nobody reviews the output. Keep a person signing off on anything that matters.</p>"""),

("is-my-business-ready",
 "How do I know if my business is ready for AI?",
 """<p>If work comes in by email and phone, you run a job management or accounting system, and the same admin jobs repeat every week, you're ready for a first step.</p>
<p>Readiness is less about technology and more about consistency. If quoting happens five different ways depending on who does it, AI will speed up the inconsistency. Warning signs that the basics need sorting first: information living in personal inboxes, no shared file structure, and no consistent job numbering. Sorting those out is the first of Workshop AI's five levels, Configure.</p>"""),

("messy-data",
 "Our information is all over spreadsheets and emails. Is AI any use yet?",
 """<p>Yes. Reading messy information and putting it into a consistent shape is one of the first places AI helps.</p>
<p>A sensible first project is getting AI to read the emails and spreadsheets you already have and put the details into your job system, rather than asking it to make decisions from scattered data. Once your tools are connected and the business sits in one picture, the bigger gains open up. Workshop AI calls this the Connect level, and nothing above it pays off until it's done.</p>"""),

("how-many-businesses-use-ai",
 "How many Australian businesses are using AI?",
 f"""<p>About 12% of Australian businesses used AI in 2024-25, according to the {a('abs', 'Australian Bureau of Statistics')} (released June 2026).</p>
<p>Use rises with size: about 35% of large businesses, 22% of medium-sized businesses and about 11% of small and micro businesses. For a 10 to 30 person trade business, that means most competitors aren't using AI in an organised way yet, which makes it a real chance to get ahead on admin speed and response times.</p>"""),

("more-work-than-it-saves",
 "Is figuring out AI more work than it saves?",
 """<p>It can be, if you try to learn every tool yourself or start with something too big. The time cost is mostly up front.</p>
<p>Picking a tool, setting it up safely, connecting it to your systems and getting the team using it the same way all take time. Keep the first project small and measurable: one admin task, with the hours it takes before and after. If it isn't saving time within a few weeks, stop or change course. Most owners bring in help not because AI is hard, but because the setup steals hours from running the business.</p>"""),
]),

("cost", "Cost and return", [
("consulting-cost",
 "How much does AI consulting cost for a trade business?",
 """<p>At Workshop AI, fixed prices start at A$1,500 to set AI up on an owner's desk, A$2,500 for a team setup and A$3,600 for a month-long Discovery. Custom builds start at A$4,400 a month or are quoted as a fixed-price project. All prices exclude GST.</p>
<p>Across the market, prices range from short workshops costing a few thousand dollars to enterprise projects running into five and six figures. For a 10 to 30 person business, be wary of anything that needs a large upfront commitment before you've seen a result in your own business.</p>"""),

("running-cost",
 "How much does AI cost to run each month?",
 """<p>For most trade businesses the ongoing software cost is modest: business plans for tools like Claude, ChatGPT and Microsoft Copilot are typically priced at tens of dollars per user per month.</p>
<p>The bigger ongoing costs come from usage-based services, such as AI phone answering charged by the minute, and from custom agents that process high volumes. These depend on how much work goes through them, so get an estimate before anything is built. Check current prices directly with the provider, because they change often.</p>"""),

("cheaper-than-admin",
 "Is AI cheaper than hiring a part-time admin person?",
 """<p>Usually it's the wrong comparison. AI takes specific repetitive tasks off your office team. It doesn't replace the person who knows your customers, sorts out the tricky invoice and keeps the office running.</p>
<p>A better question is what your office team could do with the hours AI gives back. The businesses that get most from AI use it so their existing team can handle more work as the business grows, instead of hiring the next admin role straight away.</p>"""),

("pilot",
 "Can we start small with a pilot?",
 """<p>Yes, and you should. Pick one task, agree what "done" looks like and how you'll measure it, and run it for a few weeks before committing to anything bigger.</p>
<p>Workshop AI's entry points are built for this. Claude for Owners (A$1,500) is credited in full if you go further within 60 days. Claude for Business (A$2,500) is credited in full towards Discovery within 60 days. Custom builds run month to month with no lock-in.</p>"""),

("measure-roi",
 "How do I measure whether AI is working?",
 """<p>Measure how long a task takes and how often it goes wrong, before and after.</p>
<p>Pick one or two numbers per project, such as minutes per quote, time from email to job created, invoices overdue at month end, or missed calls returned within an hour. Record a baseline for two weeks before you start. If the numbers haven't moved within a month, change the approach or stop. Avoid vague measures like "the team likes it".</p>"""),
]),

("phones", "Phones, missed calls and customers", [
("missed-calls",
 "I'm missing calls while I'm on the tools. Can AI answer them?",
 """<p>Yes. AI phone assistants can answer when you can't, take the caller's details and the job, answer common questions, and pass the job to you or book it in.</p>
<p>The simplest version is a missed-call text back, which replies by SMS when a call goes unanswered. The more advanced version is an AI receptionist that answers with a natural voice. Some job management systems now include these features, so check yours first. Before going live, decide what the assistant is allowed to promise, such as prices and arrival times, and what always goes straight to a person, such as emergencies and complaints.</p>"""),

("customers-hang-up",
 "Will customers hang up when they hear an AI voice?",
 """<p>Some will, especially people with an urgent problem. What matters most to a caller is knowing the job has been taken down and someone will get back to them.</p>
<p>Tell callers up front that they're speaking with an AI assistant, keep the call short, and make it easy to reach a person. Send emergencies straight to a human. Trial it with your own customers for a month and watch how many calls end early before deciding.</p>"""),

("ai-receptionist-cost",
 "What does an AI receptionist cost?",
 """<p>Most AI phone services charge a monthly fee, a per-minute rate, or both, and pricing changes quickly. Compare on cost per call handled, not the headline price.</p>
<p>Also check whether it books straight into your job system, whether it can hand a caller to a person mid-call, where call recordings and transcripts are stored, and how long setup and testing will take your team.</p>"""),

("call-recording-law",
 "Is it legal to record and transcribe customer calls with AI?",
 f"""<p>It can be, but recording and transcribing calls is covered by state surveillance laws and federal telecommunications law, and the rules differ between states.</p>
<p>The safe practice is to tell callers at the start that they're speaking with an AI assistant and that the call is recorded, and to cover recordings in your privacy policy. The {a('oaic_ai', 'OAIC')} also says public-facing AI tools should be clearly identified as AI. Have the wording checked if you're unsure. This is general information, not legal advice.</p>"""),

("automatic-texts-spam",
 "Can AI send automatic texts to customers without breaking spam rules?",
 f"""<p>Yes, as long as marketing messages follow the Spam Act: you need the person's consent, the message must identify your business with contact details, and every commercial message needs a working unsubscribe option, according to the {a('acma', 'ACMA')}.</p>
<p>Messages that only give factual information about a job a customer has booked, such as "your technician is on the way", are treated differently from marketing, but should still say who they're from. Anything promoting a service is marketing. This is general information, not legal advice.</p>"""),
]),

("quotes-invoices", "Quotes, invoices and getting paid", [
("ai-quotes",
 "Can I use ChatGPT or Claude to write quotes?",
 """<p>Yes, for the writing, not the pricing. AI is good at turning job notes, photos and voice memos into a clear, professional scope and quote description. It shouldn't set prices unless it's working from your own price book and rates, and a person should check every quote before it goes out.</p>
<p>The best setup puts AI inside your process: it pulls in your standard inclusions, exclusions and terms, drafts the description, and you check the numbers and send. Workshop AI's Document Standard (A$2,000 as an add-on, A$2,750 on its own) builds up to four of your client-facing documents into Claude in your own format and wording.</p>"""),

("voice-note-quote",
 "Can I send a voice note or photos from site and get a quote drafted?",
 """<p>Yes. Current AI tools can transcribe a voice note, read photos and turn them into a draft quote or invoice in your format.</p>
<p>In practice, a tradie records a two-minute voice note on site and a draft quote with scope, inclusions and exclusions is waiting in the office for pricing and sign-off. The draft still needs your prices and a human check before it goes to the customer.</p>"""),

("ai-take-off",
 "Is there AI take-off software that actually works for estimating?",
 """<p>For some trades and drawing types, AI-assisted take-off speeds up counts and measurements, but it isn't reliable enough to trust without checking, especially on complex or poorly drawn plans.</p>
<p>Treat it as a fast first pass that an estimator reviews. Before using it on live tenders, test it on past jobs where you already know the right answer.</p>"""),

("quote-liability",
 "If an AI-written quote is wrong, who's liable?",
 """<p>In most cases, your business is. The quote goes out under your business name, so the responsibility stays with you, the same as if a junior staff member had drafted it.</p>
<p>That's why AI quoting should be set up so a person checks and approves every quote, the AI works from your own price book and terms, and changes are recorded. Check your contracts and insurance too. This is general information, not legal advice.</p>"""),

("quote-follow-up",
 "Can AI follow up quotes that have gone cold?",
 f"""<p>Yes, and it's one of the simplest wins. AI can spot quotes with no reply after a set number of days, draft a follow-up in your voice that refers to the actual job, and either send it or queue it for your approval.</p>
<p>Many job management systems can trigger the reminder. AI makes the message specific to the job rather than a generic template. Keep it to two or three follow-ups and stop when the customer says no. Quote follow-ups are likely to count as commercial messages under the {a('acma', 'Spam Act')}, so include your business details and an easy way to opt out.</p>"""),

("chase-invoices",
 "Can AI chase unpaid invoices?",
 """<p>Yes. AI can check which invoices are overdue in your accounting or job system, draft reminders that mention the actual job, firm up the tone over time, and flag the ones that need a phone call.</p>
<p>Xero and most job systems already send automatic reminders. AI adds the judgement layer: a weekly list of who owes what, which customers to ring, and which disputes are real. Keep a person on anything involving a dispute or a payment plan.</p>"""),

("invoices-from-job-notes",
 "Can AI do our invoicing from job notes?",
 """<p>Partly. AI can turn completed job notes, timesheets and materials into a draft invoice, or check that everything used on a job has been billed, which catches missed materials and labour.</p>
<p>The invoice itself should still be raised in your accounting or job system so your numbers stay in one place. A good first step is having AI list completed jobs that haven't been invoiced yet.</p>"""),
]),

("software", "Simpro, ServiceM8, Xero and your other software", [
("simpro-data",
 "Can ChatGPT or Claude read our Simpro data?",
 """<p>Yes, with the right connection. Simpro has an API, so an AI assistant can be connected to read jobs, quotes, invoices and customers, and answer questions like "what's sitting in complete but not invoiced?"</p>
<p>Workshop AI connected Simpro for Mattick Air, a Melbourne commercial air conditioning business, to produce branded monthly reports for Mattick Air's own customers from live Simpro data. Start read-only: let the AI look before it's allowed to change anything.</p>"""),

("other-software",
 "Does AI work with ServiceM8, AroFlo, Tradify, Fergus, Xero and MYOB?",
 """<p>Mostly, yes. Most job management and accounting systems used by Australian tradies offer an API or integrations that let AI tools read, and sometimes write, data. What's possible depends on the system and your plan.</p>
<p>Before buying anything new, check what your current system already does and what its connections allow. Workshop AI works with the tools trade businesses already run, including Simpro, ServiceM8, AroFlo, Tradify, Fergus, Buildxact, Xero, MYOB, HubSpot, Microsoft 365 and Google Workspace.</p>"""),

("switch-software",
 "Do we have to switch software to use AI?",
 """<p>No. In most cases AI should fit around the systems you already run.</p>
<p>Switching job management software is expensive and disruptive, and it's rarely needed to get value from AI. The exception is when your current system has no way to get data in or out, or the business has outgrown it for other reasons.</p>"""),

("built-in-ai",
 "Do Simpro, ServiceM8 or Xero have AI built in already?",
 """<p>Several job management and accounting systems now include AI features, and they change often, so check your own system's latest release notes.</p>
<p>Built-in features are a good first stop because they're already connected to your data. Their limit is that each one only sees its own system. The bigger gains usually come from connecting across systems, for example from email to the job system to the accounts.</p>"""),
]),

("privacy", "Privacy, security and the law", [
("customer-details-chatgpt",
 "Can I put customer details into ChatGPT?",
 f"""<p>Not into a personal or free account, and only with care on a paid one. The {a('oaic_ai', 'OAIC')} recommends that businesses don't enter personal information, especially sensitive information, into publicly available AI tools.</p>
<p>If your team needs to use AI with customer information, use a business plan whose terms stop the provider training on or sharing your data, check those terms first, set clear rules about what can and can't go in, and cover AI in your privacy policy. Every Workshop AI setup includes written rules for using AI safely with client information.</p>"""),

("privacy-act",
 "Does the Privacy Act apply to my trade business?",
 f"""<p>It might. The Privacy Act generally covers businesses with an annual turnover over $3 million, plus some smaller ones, such as health service providers, businesses that trade in personal information and Commonwealth contractors, according to the {a('oaic_sb', 'OAIC')}.</p>
<p>A trade business with 10 to 30 staff may well turn over more than $3 million, so check where you sit. If the Act covers you, the {a('oaic_ai', 'OAIC')} says it applies to all uses of AI involving personal information. Even if you're exempt, careful handling of customer data is good practice and customers expect it. This is general information, not legal advice.</p>"""),

("training-on-data",
 "Does ChatGPT or Claude train on our business data?",
 """<p>On business and enterprise plans, the major AI providers say they don't use your business data to train their models by default. On personal and free accounts it depends on the provider and your settings, and some providers can use chats you choose to share with them, such as feedback. The terms change.</p>
<p>That's one reason to put your team on business plans with the settings checked, rather than personal accounts. Read the current terms for the plan you're on.</p>"""),

("drawings-contracts",
 "Is it safe to give AI access to our drawings, contracts and job files?",
 """<p>It can be, with the right setup: a business plan, access limited to the folders that matter, read-only to start, and no files shared with tools you haven't checked.</p>
<p>The bigger risk usually isn't the AI provider. It's staff pasting files into personal accounts or connecting apps nobody has reviewed. Decide which files the AI can read and who can use it, and keep a record of both.</p>"""),

("privacy-policy",
 "Do we need to update our privacy policy if we use AI?",
 f"""<p>Probably. The {a('oaic_ai', 'OAIC')} recommends organisations update their privacy policies and notifications to explain clearly how they use AI, and clearly identify public-facing AI tools, such as chatbots, as AI. Treat AI phone assistants the same way.</p>
<p>Say in plain words what you use AI for, which providers you use, and how customers can ask questions.</p>"""),

("shadow-ai",
 "Our staff are already using ChatGPT on their phones. Is that a problem?",
 """<p>It can be. When staff use personal AI accounts for work, customer details and business documents end up in accounts you don't control, with settings you can't see.</p>
<p>Banning it rarely works. Instead, give everyone a proper business account, a short list of what not to paste in, and a few approved uses that save them time. That's Workshop AI's first level, Configure: the right tools in place, used safely and the same way by everyone.</p>"""),
]),

("team", "Your team", [
("jobs",
 "Will AI take tradies' jobs?",
 """<p>Not the hands-on work. AI can't service an air conditioner, run cable or lay pipe.</p>
<p>Where it changes things is the office: reading emails, entering jobs, drafting quotes and chasing paperwork. In the trade businesses Workshop AI works with, the usual problem is too much admin for the people available, not too many people. AI helps the existing team keep up as the work grows.</p>"""),

("staff-buy-in",
 "How do I bring in AI without staff feeling threatened?",
 """<p>Involve them early, start with tasks they dislike, and be straight about what will and won't change.</p>
<p>Ask the office team which jobs they'd most like off their plate and make one of those the first project. Show them the result, train them properly, and keep a person in charge of every decision that matters. Workshop AI's Discovery includes a confidential team survey for this reason: the people doing the admin usually know exactly where the time goes.</p>"""),

("consult-staff",
 "Do I have to consult staff before bringing in AI?",
 f"""<p>If the change is major, you may have to. Under modern awards, an employer that decides to introduce major changes, including changes in technology, that are likely to significantly affect employees must notify them, give them written information and discuss the changes, according to the {a('fwo', 'Fair Work Ombudsman')}. Employee consent isn't required.</p>
<p>Enterprise agreements have their own consultation terms. A tool that saves some typing probably won't trigger this. One that changes people's roles might. This is general information, not legal advice.</p>"""),

("time-to-adopt",
 "How long does it take to get a team using AI?",
 """<p>A team can be set up and using a business AI tool within a week, but habits take longer. Plan on a few weeks of follow-up before it's simply how people work.</p>
<p>Workshop AI's Claude for Business is set up and running within a week, with a team intro session and a follow-up two weeks later. Custom builds take longer and are delivered one defined piece at a time.</p>"""),
]),

("tools", "Choosing AI tools", [
("which-tool",
 "ChatGPT, Claude, Copilot or Gemini: which should a trade business pay for?",
 """<p>The best choice is the one your whole team uses the same way, on a business plan, connected to your files and email. All four are capable.</p>
<p>Copilot makes sense if your business runs on Microsoft 365, and Gemini if you're on Google Workspace. Workshop AI mostly sets up Claude, because it's strong at reading long documents, writing in your own style and working with connected tools, which suits the document-heavy admin that trade businesses run on. The worst setup is everyone on a different personal account.</p>"""),

("personal-vs-business",
 "Is a personal ChatGPT or Claude account OK for work, or do we need business accounts?",
 """<p>For anything involving customer information or business documents, use a business plan.</p>
<p>Business plans give you admin control, shared workspaces and data protections that personal plans don't, and you can switch off someone's access when they leave. A personal account is fine for an owner experimenting with public information.</p>"""),

("ai-agents",
 "What is an AI agent, and does a trade business need one?",
 """<p>An AI agent is AI set up to do a defined job on its own within limits you set, such as reading every incoming work order and creating the job. Many trade businesses benefit from them, but not as the first step.</p>
<p>Agents work when the tools are connected and the process is clear. Added too early, they automate the mess. In Workshop AI's five-level path, agents come at level four, Act, after Configure, Connect and Know.</p>"""),
]),

("safety", "Safety and compliance paperwork", [
("swms",
 "Can AI write a SWMS?",
 """<p>AI can draft a Safe Work Method Statement from your templates and the job details, which saves time, but the business doing the work must prepare the SWMS before high-risk construction work starts, in consultation with the workers involved.</p>
<p>Someone who knows the site should review and adjust every AI draft, because generic AI output isn't fit to use unchecked. Use AI for the first draft and for consistency across jobs, not for the hazard assessment itself.</p>"""),

("compliance-certificates",
 "Can AI fill in compliance certificates for electrical or plumbing work?",
 """<p>It can pre-fill details from job records and check for missing information, but the licensed person must still check and sign it, and lodge it where the rules require.</p>
<p>Compliance certificates are the licence holder's responsibility. AI can cut the typing and catch gaps. It can't take the accountability.</p>"""),

("site-questions",
 "Can AI help our team answer safety and technical questions on site?",
 """<p>Yes, if it answers from your own documents: procedures, manuals, SWMS and manufacturer specifications. A technician can ask on their phone and get an answer that points to the document it came from.</p>
<p>Don't rely on any answer the AI can't point to a source for, and confirm anything safety-critical with a supervisor.</p>"""),
]),

("industries", "AI by industry", [
("hvac",
 "How can an HVAC business use AI?",
 """<p>Common wins for HVAC and refrigeration businesses are reading work orders that arrive by email in many formats and creating the job, producing maintenance and compliance reports for commercial clients, drafting quotes from service notes, and keeping recurring maintenance on track.</p>
<p>For Mattick Air, a Melbourne commercial air conditioning business, Workshop AI built an agent that reads every emailed work order and lands the job ready to go, with a person staying on the trigger, plus branded monthly customer reports built from live Simpro data.</p>"""),

("plumbing",
 "How can a plumbing business use AI?",
 """<p>The biggest wins for plumbers are usually after-hours and missed calls, drafting quotes from photos and voice notes, and chasing quotes and invoices.</p>
<p>An AI assistant can take the caller's details, the problem and how urgent it is, then send it to the right person. Emergencies such as burst pipes or suspected gas leaks should always go straight to a person. AI can also prepare job paperwork from your records, while compliance certificates stay with the licensed plumber.</p>"""),

("electrical",
 "How can an electrical contractor use AI?",
 """<p>Electrical contractors use AI to draft quotes from site notes and drawings, read builder and client emails into jobs, keep track of variations, and prepare test and compliance paperwork for the licensed electrician to check.</p>
<p>AI can also answer technical questions from your own manuals and procedures. Certificates and sign-offs stay with the licence holder.</p>"""),

("construction",
 "How can a builder or construction company use AI?",
 """<p>Builders get the most from AI by finding information across job folders (drawings, RFIs, variations and contracts), drafting variations, RFIs and site reports, checking tender documents, and keeping SWMS consistent.</p>
<p>The biggest win for many builders is being able to ask "what did we agree about this on that job?" and get an answer that points to the document it came from. This works best when job files are organised consistently.</p>"""),

("logistics",
 "How can a logistics or transport business use AI?",
 """<p>Logistics businesses use AI to read booking requests and manifests from emails into their system, handle same-day changes, draft customer updates, check proof-of-delivery paperwork against invoices, and report on late or failed deliveries.</p>
<p>Route optimisation itself is usually better handled by dedicated routing software. AI is strongest on the paperwork and communication around it.</p>"""),

("industrial",
 "How can a manufacturing or industrial business use AI?",
 """<p>Industrial businesses use AI for the paperwork around the work: reading requests for quotes and purchase orders, drafting quotes from specifications, matching supplier documents to orders, and keeping quality, maintenance and compliance records consistent.</p>
<p>The pattern is the same as in the trades: start with the office job that repeats most, connect AI to the systems you already use, and keep a person signing off.</p>"""),

("hospitality-services",
 "Can AI help restaurants and service businesses too?",
 """<p>Yes. The same patterns apply: bookings and enquiries, rostering admin, supplier invoices, stock and ordering paperwork, and customer messages.</p>
<p>Workshop AI works mostly with trades, construction and logistics, and also with hospitality and other service businesses where the office load looks similar.</p>"""),
]),

("getting-found", "Getting found and marketing", [
("show-up-in-ai",
 "Why doesn't my business show up when people ask ChatGPT or Google's AI?",
 """<p>AI assistants recommend businesses they can find clear, consistent and checkable information about. Common gaps are no Google Business Profile, a website that doesn't say plainly what you do and where, few reviews, and few mentions on other sites.</p>
<p>The fixes: state on your website who you serve, where, and what it costs; keep your business name, location and phone number the same everywhere; build up genuine reviews; and answer the questions your customers actually ask, on your own site.</p>"""),

("review-replies",
 "Can AI reply to our Google reviews?",
 """<p>Yes. AI can draft replies in your voice quickly, which makes it easier to reply to every review. Read each one before posting, because a generic reply to a detailed complaint does more harm than no reply.</p>
<p>Never use AI to write fake reviews. Fake reviews are misleading under the Australian Consumer Law and breach platform rules.</p>"""),
]),

("getting-help", "Getting help, and working with Workshop AI", [
("consultant-or-diy",
 "Do I need an AI consultant, or can I do it myself?",
 """<p>You can do a lot yourself: sign up to a business plan, learn the basics and try it on your own admin.</p>
<p>Bring in help when you want the whole team set up safely and consistently, when AI needs connecting to your job and accounting systems, or when you don't have the hours to work it out. A good consultant leaves you able to run things without them.</p>"""),

("consultant-red-flags",
 "Are AI consultants worth it, or a scam?",
 """<p>Some are worth it and some aren't. The warning signs are big upfront fees before you've seen anything work, slide decks instead of working software, buzzwords you can't repeat to your team, lock-in contracts and vague outcomes.</p>
<p>Ask for fixed prices, a clear definition of done, a real example from a business like yours, and month-to-month terms.</p>"""),

("government-help",
 "Is there government funding or free help for AI in a small business?",
 f"""<p>There is some low-cost help. The Australian Government's {a('asbas', 'Digital Solutions program')} offers small businesses with fewer than 20 employees up to five hours of one-to-one advice for a small fee, and AI is one of its topics.</p>
<p>In Victoria it's delivered by Melbourne Innovation Centre. Check business.gov.au for current details. Business Victoria and local councils also run programs from time to time. Ask your accountant how AI spending is treated for tax.</p>"""),

("what-is-workshop-ai",
 "What does Workshop AI do?",
 """<p>Workshop AI is a Melbourne AI implementation consultancy for Australian tradies and trade, service and industrial businesses.</p>
<p>It sets up AI tools such as Claude safely for owners and teams, maps how the business really runs, and builds custom AI agents and automations into the systems the business already uses, such as Simpro, ServiceM8 and Xero. Prices are fixed and start at A$1,500 (ex GST). See the <a href="/facts/">company facts</a> for the full picture.</p>"""),

("where-based",
 "Where is Workshop AI based, and do you work outside Melbourne?",
 """<p>Workshop AI is based in Hobsons Bay in Melbourne's western suburbs, close to Altona, Williamstown, Newport, Laverton and the western industrial areas.</p>
<p>We visit businesses in person anywhere around Melbourne and deliver remotely anywhere in Australia.</p>"""),

("how-to-start",
 "How does working with Workshop AI start?",
 f"""<p>With a free 30-minute chat, in person around Melbourne or by video. We talk through how the business runs and tell you which of the five levels you're really on.</p>
<p>If there's a fit, we pick one real problem and fix it end to end before anything bigger is on the table. No lock-in. <a href="{ORG['booking_url']}" rel="noopener" target="_blank">Book a time</a>, email <a href="mailto:{ORG['email']}">{ORG['email']}</a> or call Justin on <a href="tel:{ORG['phone_intl']}">{ORG['phone_display']}</a>.</p>"""),
]),
]
