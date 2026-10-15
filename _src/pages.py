"""Content for the industry, local and Simpro pages.

Each page is built by _src/build.py into its own folder, in the same style as
/facts/. Rules, as for data.py:
- Australian spelling, no em dashes.
- No figure or rule without a source we have read (listed in "sources").
- No invented client results. Mattick Air is the only named client.
- Answer first. Every page must pass the doorway test: if you could swap the
  trade or place name and nothing else needed to change, rewrite it.
"""


def L(url, text):
    return f'<a href="{url}" rel="noopener" target="_blank">{text}</a>'


# Sources, read October 2026
ARC_RTA = "https://arctick.org/information/faqs/rta/"
ARC_CONDITIONS = "https://www.arctick.org/business-authorisation/conditions-of-authorisation/"
VIC_COOLING = "https://health.vic.gov.au/water/section-4-cooling-tower-risk-management-plans-legal-responsibilities"
BPC_ESM = "https://www.bpc.vic.gov.au/resource-hub/safety-guides/essential-safety-measures"
BPC_CERTS = "https://www.bpc.vic.gov.au/plumbers/delivering-safe-and-compliant-plumbing/compliance-certificates"
BPC_CLASSES = "https://www.bpc.vic.gov.au/plumbers/plumber-classes-and-categories"
CAV_RENTAL_GAS = "https://www.consumer.vic.gov.au/housing/renting/repairs-alterations-safety-and-pets/gas-electrical-and-water-safety-standards/rental-providers-gas-and-electrical-safety"
YVW_BACKFLOW = "https://yvw.com.au/help-advice/backflow-prevention/testing-and-reporting"
SEW_BACKFLOW = "https://southeastwater.com.au/content/dam/web/building-and-development/builders-and-plumbers/Backflow%20Test%20Report%20Form.pdf"
VIC_ELECTRIFY = "https://www.energy.vic.gov.au/households/electric-and-efficiency-standards-for-buildings"
ESV_GAS_BPC = "https://www.energysafe.vic.gov.au/about-us/our-organisation/working-others/victorian-building-authority"
ESV_COES = "https://www.energysafe.vic.gov.au/certificates-electrical-safety/certificates-electrical-safety-consumers"
ESV_PRESCRIBED = "https://www.energysafe.vic.gov.au/certificates-electrical-safety/obligations-and-guidelines/prescribed-and-non-prescribed-work"
ESV_CONNECT = "https://www.energysafe.vic.gov.au/certificates-electrical-safety/esvconnect-certificates-electrical-safety"
ESV_REC = "https://www.energysafe.vic.gov.au/licensing/electrical-licences/licence-types/registered-electrical-contractors-rec"
SOLAR_VIC = "https://www.solar.vic.gov.au/node/72"
SOP_CLAIM = "https://www.bpc.vic.gov.au/builders/security-of-payment/making-a-payment-claim-under-the-sop-act"
SOP_CHANGES = "https://www.bpc.vic.gov.au/builders/security-of-payment/changes-to-the-sop-act/changes-to-the-sop-scheme"
SOP_RESPOND = "https://www.bpc.vic.gov.au/builders/security-of-payment/responding-to-a-payment-claim-under-the-sop-act"
SOP_OVERVIEW = "https://www.bpc.vic.gov.au/builders/security-of-payment/overview-of-security-of-payment"
CAV_VARIATIONS = "https://consumer.vic.gov.au/licensing-and-registration/builders-and-tradespeople/checklists/working-with-your-building-client"
CAV_NEW_LAWS = "https://www.consumer.vic.gov.au/latest-news/new-domestic-building-contract-laws-passed-in-victoria"
WORKSAFE_SWMS = "https://worksafe.vic.gov.au/safe-work-method-statements-swms"
NHVR_PRIMARY = "https://www.nhvr.gov.au/safety-accreditation-compliance/chain-of-responsibility/regulatory-advice/the-primary-duty"
NHVR_LAW = "https://www.nhvr.gov.au/law-policies/heavy-vehicle-national-law-and-regulations"
NHVR_RECORDS = "https://www.nhvr.gov.au/safety-accreditation-compliance/fatigue-management/record-keeping-requirements"
NHVR_FALSE = "https://www.nhvr.gov.au/safety-accreditation-compliance/chain-of-responsibility/regulatory-advice/providing-false-or-misleading-information-to-the-nhvr"
NTC_HVNL = "https://ntc.gov.au/laws-and-regulations/heavy-vehicle-national-law"
ADG_VIC = "https://ablis.business.gov.au/service/vic/australian-code-for-the-transport-of-dangerous-goods-by-road-and-rail-adg-code-/24496"
CARIO_SURCHARGES = "https://cario.com.au/resources/hidden-freight-costs-where-to-look"
ECON_HB = "https://economy.id.com.au/hobsons-bay"
ECON_HB_JOBS = "https://economy.id.com.au/hobsons-bay/employment-by-industry"
VIC_WIP = "https://www.planning.vic.gov.au/__data/assets/pdf_file/0033/637836/western_chapter04_productivity.pdf"
POM = "https://www.portofmelbourne.com/?p=9119"
WGT = "https://www.premier.vic.gov.au/west-gate-tunnel-now-open"
ASBAS = "https://business.gov.au/expertise-and-advice/digital-solutions-australian-small-business-advisory-services"
HB_BUSINESS = "https://www.hobsonsbaybusiness.com.au/Do-Business/Workshops-and-Events"
LEADWEST = "https://leadwest.com.au"
WYNDHAM_IGNITE = "https://www.wyndham.vic.gov.au/node/23919"
SIMPRO_API_FAQ = "https://helpguide.simprogroup.com/Content/Service-and-Enterprise/API-FAQs.htm"
SIMPRO_API_DOCS = "https://developer.simprogroup.com/apidoc/"
SIMPRO_LIMITS = "https://developer.simprogroup.com/apidoc/?page=ed8457e003ba0f6197756eca5a61fde9"
SIMPRO_PAGING = "https://developer.simprogroup.com/apidoc/?page=07adc9c3c19b7c17e7309e86c22161a2"
SIMPRO_AUTH = "https://developer.simprogroup.com/apidoc/?page=b0d64c044a432c8e0f9f01e0641d5596"
SIMPRO_LIGHTNING_PR = "https://www.simprogroup.com/company/press/simpro-group-unveils-lightning"
SIMPRO_LIGHTNING = "https://www.simprogroup.com/lightning"
SIMPRO_RAIN = "https://www.simprogroup.com/rain"
SIMPRO_RAIN_PR = "https://www.simprogroup.com/company/press/simpro-group-announces-rain"
SIMPRO_PRICING = "https://www.simprogroup.com/au/pricing"
SIMPRO_STAGES = "https://helpguide.simprogroup.com/Content/Service-and-Enterprise/Managing-Existing-Jobs.htm"
SIMPRO_QUOTES = "https://helpguide.simprogroup.com/Content/Service-and-Enterprise/View-Quotes.htm"
SIMPRO_GLOSSARY = "https://helpguide.simprogroup.com/articles/help-guide/simpro-glossary"
SIMPRO_ABOUT = "https://www.simprogroup.com/company/about-us"
ZAPIER_SIMPRO = "https://zapier.com/apps/simpro/integrations"
ZAPIER_SIMPRO_PARTNER = "https://www.simprogroup.com/partners/integration-partners/zapier"
ZAPIER_MCP = "https://zapier.com/mcp/simpro"
VIASOCKET_MCP = "https://viasocket.com/mcp/simpro"
TUGGER = "https://marketplace.simprogroup.com/apps/tugger"
TUGGER_BLOG = "https://tuggerapp.com/Blogs/Blog/how-to-connect-simpro-to-ai"


# ---------------------------------------------------------------------------
PAGES = [

# ============================================================== HVAC
{
"slug": "ai-for-hvac",
"short": "HVAC and refrigeration",
"audience": "HVAC, air conditioning and refrigeration businesses",
"title": "AI for HVAC and refrigeration businesses, Melbourne | Workshop AI",
"description": ("How HVAC and refrigeration businesses use AI for work orders, maintenance reports, "
                "refrigerant and cooling tower records and quotes, with a real Melbourne example. "
                "Works with Simpro, AroFlo and ServiceM8."),
"eyebrow": "AI for HVAC and refrigeration",
"h1": "AI for HVAC and refrigeration businesses",
"lede": ("In an HVAC business, AI earns its keep in the office: turning emailed work orders into jobs, "
         "writing up maintenance reports for commercial clients, keeping refrigerant and cooling tower "
         "records in order, and drafting quotes from technicians' notes. Here's where it fits, where it "
         "doesn't, and what we built for a Melbourne commercial air conditioning business."),
"sections": [
("where-time-goes", "Where the time goes", "Five office jobs AI handles well in HVAC", """
<ul>
<li><strong>Work orders.</strong> Facility managers, builders and agents send work orders by email in every format: PDFs, portal notifications, a line in the body of an email. AI reads each one, pulls out the site, asset, fault, priority and order number, and sets up the job for a person to check.</li>
<li><strong>Planned maintenance.</strong> Commercial maintenance contracts mean recurring visits across many sites. AI can check the schedule against what each contract promises, flag sites that are overdue, and draft service reports from technicians' notes, readings and photos.</li>
<li><strong>Customer reporting.</strong> Facility managers want regular reports on their plant: what was serviced, readings taken, faults found and what you recommend replacing. AI can produce them from live job data, in your branding, every month.</li>
<li><strong>Quotes from service notes.</strong> A technician's note such as "condenser fan motor seized, unit 3" becomes a clear quote description with your standard inclusions, exclusions and terms. Prices come from your own price book, and a person checks every quote before it goes out.</li>
<li><strong>Breakdown peaks.</strong> When the weather turns, breakdown calls and emails spike. AI can sort the inbox and after-hours messages into breakdowns, routine service and quote requests, so urgent jobs reach a person first.</li>
</ul>
"""),
("compliance", "Compliance records", "What AI can prepare, and what stays with you", f"""
<p>HVAC carries more record-keeping than most trades. AI is good at keeping those records complete and on time. It can't hold the licence or make the safety call.</p>
<h3>Refrigerant records</h3>
<p>A business that buys, stores or disposes of refrigerant needs a Refrigerant Trading Authorisation from the {L(ARC_RTA, 'Australian Refrigeration Council')}. The {L(ARC_CONDITIONS, 'authorisation conditions')} require records of refrigerant bought, recovered, sold and disposed of, equipment checks and maintenance, the technicians who handled your refrigerant and cylinder test dates, supplied within 14 days if ARC asks. Your authorisation number also has to appear on documents such as quotes and invoices.</p>
<p>AI can compile those records from job and stock data each quarter and flag the gaps, such as a job that used refrigerant with no recovery recorded, or a cylinder due for testing. The authorisation holder stays responsible for them.</p>
<h3>Cooling towers</h3>
<p>In Victoria, cooling towers fall under the Public Health and Wellbeing Regulations 2019. According to the {L(VIC_COOLING, 'Department of Health')}, each system needs a risk management plan that is reviewed and independently audited every year, monthly inspections and colony count tests, and Legionella testing every three months, with action required when results exceed set levels.</p>
<p>If you look after cooling towers for clients, AI can track every test due date, read lab results as they arrive, flag any result above an action level the moment it lands, and draft the records for the responsible person to check. The response to a failed test belongs to people, following the site's risk management plan.</p>
<h3>Essential safety measures and compliance certificates</h3>
<p>Owners of buildings other than houses must prepare an annual essential safety measures report, and the {L(BPC_ESM, 'Building and Plumbing Commission')} says an agent such as the maintenance contractor can complete it. Air handling systems used for smoke control and mechanical ventilation with a cooling tower are on the list. AI can assemble your maintenance records into the format each owner needs.</p>
<p>Mechanical services and refrigerated air-conditioning are {L(BPC_CLASSES, 'plumbing classes in Victoria')}, so {L(BPC_CERTS, 'compliance certificate rules')} apply: any job over $750 including materials, labour and GST, and any cooling tower work regardless of value. AI can flag which completed jobs need one and pre-fill it. Only the licensed practitioner can issue and lodge it.</p>
"""),
("example", "Client example", "Mattick Air, Melbourne", """
<div class="card">
<p><strong>Mattick Air</strong> is a Melbourne commercial air conditioning business. Work orders arrived by email all day in a dozen different formats, and every one was read by a person and retyped into the job system by hand.</p>
<p>Workshop AI built an agent that reads every work order and lands the job ready to go, with a person staying on the trigger. Workshop AI has also built branded monthly reports for Mattick Air's own customers, produced from live Simpro data.</p>
</div>
"""),
("software", "Systems", "Works with the HVAC software you already run", """
<p>Simpro, AroFlo, ServiceM8, Fergus, Tradify and Ascora all sell versions of their job management software to Australian HVAC businesses, several with refrigerant logging and maintenance planning built in. AI doesn't replace them. It reads from them, writes to them where that's safe, and connects them to your email and accounts.</p>
<p>Running Simpro? See <a href="/simpro-ai/">using AI with Simpro</a>, including what Simpro's own AI does and doesn't cover.</p>
"""),
],
"faqs": [
("work-order-portals", "Can AI read work orders from facility management portals as well as email?",
 """<p>Usually, yes. Most portals send an email or PDF for each new work order, and AI reads those the same way it reads any other email. Where a portal offers an export or API, AI can read from that directly.</p>
<p>Start with a person confirming each job before it's created. Once the extraction is reliable, the person moves to checking exceptions only.</p>"""),
("refrigerant-records", "Can AI keep our refrigerant records for ARC?",
 f"""<p>It can do the compiling. AI can pull refrigerant use, recovery and disposal from job and stock records each quarter and flag missing entries, so the records the {L(ARC_CONDITIONS, 'authorisation conditions')} require are ready if ARC asks for them within 14 days.</p>
<p>The authorisation holder is still responsible for the records being accurate, so someone should check each quarter's figures before they're filed.</p>"""),
("service-reports", "Can AI write our maintenance and service reports?",
 """<p>Yes, as drafts. AI turns a technician's notes, readings and photos into a consistent report in your format, and can roll individual visits into a monthly report for each commercial client.</p>
<p>The technician or a supervisor should check anything that records a fault, a reading or a recommendation before it goes to the client.</p>"""),
("cooling-tower-results", "Should AI decide what to do about a failed cooling tower test?",
 f"""<p>No. AI should flag the result immediately and start the response steps from the site's risk management plan, but the decisions belong to the people responsible under Victoria's {L(VIC_COOLING, 'cooling tower rules')}.</p>
<p>Where AI earns its keep is cutting the risk of a result sitting unread in an inbox or a test date slipping past.</p>"""),
("hvac-cost", "What does it cost to start using AI in an HVAC business?",
 """<p>Workshop AI's Claude for Owners starts at A$1,500 and Claude for Business at A$2,500, both fixed price. Custom builds, such as a work order agent connected to your job system, start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project. All prices exclude GST.</p>"""),
],
},

# ============================================================== Plumbing
{
"slug": "ai-for-plumbing",
"short": "Plumbing and gas",
"audience": "plumbing and gasfitting businesses",
"title": "AI for plumbing and gas businesses, Melbourne | Workshop AI",
"description": ("How plumbing and gas businesses in Victoria use AI for missed calls, quotes, compliance "
                "certificates, backflow tests and rental gas safety checks, with licensed work kept with "
                "the licensed plumber."),
"eyebrow": "AI for plumbing and gas",
"h1": "AI for plumbing and gas businesses",
"lede": ("For plumbing and gas businesses, AI helps most with the calls you can't answer, the quotes you "
         "write at night, and the certificates and test reports that pile up after the job. Licensed "
         "work and sign-offs stay with the licensed plumber."),
"sections": [
("where-time-goes", "Where the time goes", "Five office jobs AI handles well in plumbing", f"""
<ul>
<li><strong>Missed and after-hours calls.</strong> An AI assistant can take the caller's name, address, the problem and how urgent it is, then send it to whoever is on call. Burst pipes and suspected gas leaks are set up to go straight to a person.</li>
<li><strong>Quotes from photos and voice notes.</strong> A photo of a failed hot water unit or a voice memo from a blocked drain becomes a clear quote description with your standard inclusions and exclusions. Prices come from your price book, checked by a person.</li>
<li><strong>Rental gas safety checks.</strong> Victorian rental providers must have a {L(CAV_RENTAL_GAS, 'gas safety check every two years')} by a gasfitter licensed or registered for Type A appliance servicing. For plumbers who do this work, AI can manage the cycle: due dates, booking access with tenants and property managers, and sending the report.</li>
<li><strong>Backflow testing.</strong> Testable backflow devices at the meter must be {L(YVW_BACKFLOW, 'tested every 12 months')}, with results reported on the water corporation's form, and a failed device must be repaired and retested within {L(SEW_BACKFLOW, '20 business days')}. AI can track due dates, pre-fill the forms from test data and flag failures so the retest is booked.</li>
<li><strong>Chasing quotes.</strong> Hot water and drainage quotes often go quiet while the customer shops around. AI drafts follow-ups in your voice and keeps a list of who needs a call, so fewer quotes stall for want of a reminder.</li>
</ul>
"""),
("compliance", "Compliance certificates", "What AI can do, and what stays with the licence holder", f"""
<p>In Victoria, a {L(BPC_CERTS, 'compliance certificate')} is required for any plumbing job over $750, counting materials, labour and GST. It's required regardless of value for Type A gas appliance installation, relocation or replacement, fuel conversions, consumer gas piping, below-ground sanitary drains and cooling tower work.</p>
<p>Only a licensed plumber can issue one. The customer must get it within five days of the work being completed, and it must be lodged with the Building and Plumbing Commission within five days, through VBA360. Certificates bought from 22 September 2025 expire 12 months after purchase.</p>
<p>That's a lot of five-day deadlines. AI can check every completed job against the rules, list the certificates due each day, pre-fill them from the job record, chase technicians for missing details, and flag unused certificates before they expire. The licensed plumber reviews, signs and lodges. More complex Type B gas work needs {L(ESV_GAS_BPC, 'Energy Safe Victoria')}'s acceptance before gas is supplied, and AI can assemble the paperwork for that too.</p>
"""),
("whats-changing", "What's changing", "Gas hot water questions are coming", f"""
<p>The Victorian Government says that from 1 March 2027, gas water heaters in existing homes will need to be {L(VIC_ELECTRIFY, 'replaced with electric ones at the end of their life')}, with some exemptions. Customers will ask what that means for them.</p>
<p>AI can help you answer consistently: drafting clear quote options for electric replacements, a short explainer in your own words, and replies to the questions you hear every week. Check the current rules and rebates before anything goes out, because the details and exemptions are set by government and can change.</p>
"""),
("first-project", "A sensible first project", "A compliance certificate tracker", """
<div class="card">
<p>Every completed job is checked overnight against the certificate rules. Each morning the office gets a short list: certificates due, with the deadline, a pre-filled draft for each, and any job missing details the plumber needs to supply.</p>
<p>It's narrow, it uses data you already have, and it reduces a deadline risk. Once it works, the same pattern extends to backflow due dates and rental gas safety checks.</p>
</div>
"""),
("software", "Systems", "Works with the plumbing software you already run", """
<p>Simpro, ServiceM8, Fergus, Tradify, AroFlo and Ascora all sell to Australian plumbing businesses. Simpro and ServiceM8 both advertise compliance certificates in the app, and Simpro includes backflow testing in its maintenance planning. AI works alongside them rather than replacing them. If you run Simpro, see <a href="/simpro-ai/">using AI with Simpro</a>.</p>
"""),
],
"faqs": [
("ai-receptionist-emergencies", "Can an AI receptionist handle emergency plumbing calls?",
 """<p>It can take the details and route the call, but emergencies should reach a person straight away. Set it up so a burst pipe, flooding or a suspected gas leak is put through or escalated immediately, never queued.</p>
<p>Tell callers they're speaking with an AI assistant. The <a href="https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products" rel="noopener" target="_blank">OAIC</a> recommends clearly identifying public-facing AI tools as AI.</p>"""),
("certificate-prefill", "Can AI fill in a plumbing compliance certificate?",
 f"""<p>It can pre-fill one from the job record and check nothing is missing, which is most of the typing. The licensed plumber must check, issue and lodge it, within the {L(BPC_CERTS, 'five-day timeframes')}.</p>"""),
("backflow-reports", "Can AI help with backflow test reports?",
 f"""<p>Yes. AI can keep the register of devices and due dates, pre-fill each water corporation's form from the tester's results, and flag any failed device so the repair and retest happen within the {L(SEW_BACKFLOW, '20 business days')} allowed. The tester and the licensed plumber still sign.</p>"""),
("hot-water-electrification", "How should we handle customers asking about replacing gas hot water?",
 f"""<p>Give them a consistent, accurate answer. AI can draft your quote options and a plain-English explainer, but check it against the {L(VIC_ELECTRIFY, "government's current rules")} and rebate information before sending, and update it when they change.</p>"""),
("plumbing-cost", "What does it cost to start using AI in a plumbing business?",
 """<p>Workshop AI's Claude for Owners starts at A$1,500 and Claude for Business at A$2,500, both fixed price. Custom builds, such as a certificate tracker connected to your job system, start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project. All prices exclude GST.</p>"""),
],
},

# ============================================================== Electrical
{
"slug": "ai-for-electrical",
"short": "Electrical",
"audience": "electrical contractors",
"title": "AI for electrical contractors, Melbourne | Workshop AI",
"description": ("How electrical contractors in Victoria use AI for quotes, builder variations, security of "
                "payment claims and Certificates of Electrical Safety, with testing and sign-off kept with "
                "the licensed electrician."),
"eyebrow": "AI for electrical contractors",
"h1": "AI for electrical contractors",
"lede": ("Electrical contractors spend their office hours on quotes, builder emails and variations, "
         "progress claims, and Certificates of Electrical Safety with legal deadlines. AI can draft and "
         "track all of it. Testing, certification and sign-off stay with the licensed electrician."),
"sections": [
("where-time-goes", "Where the time goes", "Five office jobs AI handles well for sparkies", f"""
<ul>
<li><strong>Quotes and scopes.</strong> AI reads specifications, scope documents and builder emails, lists inclusions and exclusions, spots items the scope doesn't cover, and drafts the quote letter. Counting fittings from drawings is still best done in estimating software, and prices come from your own rates.</li>
<li><strong>Builder instructions and variations.</strong> Site instructions arrive by email, text and in conversation. AI captures each one against the job, drafts the variation the same day, and keeps a register so less work gets done and never billed.</li>
<li><strong>Progress claims.</strong> As a subcontractor you're usually covered by Victoria's {L(SOP_OVERVIEW, 'security of payment laws')}. AI can draft each month's claim from job data with the wording the Act requires, and track when the builder's payment schedule is due.</li>
<li><strong>Solar and battery paperwork.</strong> Jobs under Solar Victoria programs come with {L(SOLAR_VIC, 'their own requirements')}, including installer accreditation and the customer's QR code. AI can run a checklist on every job so missing paperwork is caught before it holds up the rebate.</li>
<li><strong>Technical questions from your own documents.</strong> AI can answer from your procedures, manufacturer instructions and past jobs, pointing to the document it used, so apprentices get an answer without ringing the boss.</li>
</ul>
"""),
("coes", "Certificates of Electrical Safety", "What AI can prepare, and what stays with the electrician", f"""
<p>In Victoria a Certificate of Electrical Safety is a legal document recording the electrical work done, and {L(ESV_COES, 'Energy Safe')} says failing to meet the certificate requirements is a criminal offence. Certificates are completed electronically through {L(ESV_CONNECT, 'ESVConnect')}, and work done for profit is certified under a registered electrical contractor.</p>
<p>{L(ESV_PRESCRIBED, 'Prescribed work')}, which includes consumer mains, solar and battery systems, high-voltage work and hazardous areas, must also be inspected by a licensed electrical inspector before it's connected. For non-prescribed work, copies go to the customer and Energy Safe within a month of completion.</p>
<p>AI can list which completed jobs need a certificate, pre-fill the details from the job record, chase the electrician for anything missing, and track every deadline. It must never invent a test result. The licensed electrician enters the results, completes the certificate and submits it.</p>
"""),
("payment-claims", "Getting paid", "Security of payment claims, on time and in the right form", f"""
<p>Under Victoria's Security of Payment Act, a {L(SOP_CLAIM, 'payment claim')} must identify the work, state the amount and say it is a payment claim under the Building and Construction Industry Security of Payment Act 2002. Since {L(SOP_CHANGES, '15 April 2026')} you can make one claim a month, served from the last day of the month.</p>
<p>If the builder doesn't give a {L(SOP_RESPOND, 'payment schedule')} within 10 business days, they become liable for the full amount claimed. That makes on-time, correctly worded claims worth real money. AI can draft them from your job data each month and remind you when a schedule is overdue. This is general information, not legal advice.</p>
"""),
("first-project", "A sensible first project", "A variations and claims register", """
<div class="card">
<p>Every builder email and site instruction is read into one register against the right job. Variations are drafted the same day for you to approve, and at the end of the month the register becomes a draft payment claim with the required wording.</p>
<p>It's narrow, it uses information you already receive, and it cuts the chance of work slipping through unbilled. Once it's working, the same register can track which jobs still need a Certificate of Electrical Safety.</p>
</div>
"""),
("software", "Systems", "Works with the software electricians already run", f"""
<p>{L(SIMPRO_ABOUT, 'Simpro')} was started in 2002 by an electrical business owner and a software engineering student, and it still sells to electrical contractors, as do AroFlo, Fergus, ServiceM8 and Tradify. AI works with these systems rather than replacing them. If you run Simpro, see <a href="/simpro-ai/">using AI with Simpro</a>.</p>
"""),
],
"faqs": [
("coes-ai", "Can AI fill in a Certificate of Electrical Safety?",
 f"""<p>It can pre-fill the job details and check for gaps, but the licensed electrician must enter the test results, complete it and submit it through {L(ESV_CONNECT, 'ESVConnect')}. AI should never generate test results.</p>"""),
("quote-from-drawings", "Can AI quote from electrical drawings?",
 """<p>Partly. AI is good at reading specifications and scope documents, finding gaps and drafting the quote. Counting symbols on drawings is more reliable in estimating software built for takeoffs. Combine the two, and price from your own rates.</p>"""),
("payment-claims-ai", "Can AI write our progress claims to builders?",
 f"""<p>Yes, as drafts. AI can build each month's claim from job data and include the wording the {L(SOP_CLAIM, 'Act requires')}, so claims go out on time and in the right form. Check each claim before it's served. This is general information, not legal advice.</p>"""),
("standards-questions", "Can AI answer technical questions about the Wiring Rules?",
 """<p>Use it carefully. AI tools can be wrong on clause-level detail. Point AI at your own procedures and the manufacturer documents you hold, have it show where each answer came from, and check the standard itself for anything that matters.</p>"""),
("electrical-cost", "What does it cost to start using AI in an electrical business?",
 """<p>Workshop AI's Claude for Owners starts at A$1,500 and Claude for Business at A$2,500, both fixed price. Custom builds, such as a variations and claims register connected to your job system, start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project. All prices exclude GST.</p>"""),
],
},

# ============================================================== Construction
{
"slug": "ai-for-construction",
"short": "Construction and building",
"audience": "builders and construction companies",
"title": "AI for builders and construction companies, Melbourne | Workshop AI",
"description": ("How Victorian builders and construction companies use AI to find answers across job "
                "files, draft variations, RFIs and site reports, keep SWMS current and prepare security of "
                "payment claims."),
"eyebrow": "AI for builders and construction",
"h1": "AI for builders and construction companies",
"lede": ("For builders and construction companies, AI is best at the document load: finding what was "
         "agreed across job folders, drafting variations, RFIs and site reports, keeping SWMS current, and "
         "getting payment claims and schedules out on time. Site decisions, prices and sign-offs stay "
         "with your people."),
"sections": [
("where-time-goes", "Where the time goes", "Five document jobs AI handles well in construction", f"""
<ul>
<li><strong>Finding what was agreed.</strong> Drawings, RFIs, variations, contracts and emails sit across folders and inboxes. AI can answer "what did we agree about the window change on that job?" and point to the document it came from.</li>
<li><strong>Variations.</strong> For domestic work in Victoria, a variation generally has to be {L(CAV_VARIATIONS, 'agreed in writing')} on a variation notice, with the new price and completion date, before the work is done. AI drafts the notice from site notes, and a register shows which variations are still waiting on a price or a signature before anyone starts.</li>
<li><strong>Payment claims and schedules.</strong> Whether you're claiming or receiving claims, the {L(SOP_OVERVIEW, 'security of payment')} timeframes are tight. AI can draft claims in the required form and list every claim you've received with the date its payment schedule is due.</li>
<li><strong>Site diaries, RFIs and defects.</strong> A supervisor's voice note and photos become a diary entry, an RFI or a defect item, filed against the job. Defect lists are tracked to close-out, which often decides when you get paid.</li>
<li><strong>Tenders.</strong> AI reads tender documents for scope gaps, special conditions, insurance requirements and deadlines, so they're in front of you when you price.</li>
</ul>
"""),
("rules", "The rules AI helps you keep", "Variations, payment claims and SWMS", f"""
<h3>Security of payment</h3>
<p>Victoria's security of payment scheme covers most construction contracts, including subcontracts, but not a builder's contract with a home owner. A {L(SOP_CLAIM, 'payment claim')} must identify the work, state the amount and say it's made under the Building and Construction Industry Security of Payment Act 2002. Since {L(SOP_CHANGES, '15 April 2026')}, claims are monthly, served from the last day of the month, and can be made for up to six months after practical completion.</p>
<p>If you receive a claim, a {L(SOP_RESPOND, 'payment schedule')} is due within 10 business days, or you become liable for the full amount. An AI register of incoming claims with their deadlines is cheap insurance.</p>
<h3>Domestic building contracts</h3>
<p>Changes to Victoria's domestic building contract laws, including a single variation process, were {L(CAV_NEW_LAWS, 'passed in 2025')}, with the start date set by the government. AI-drafted templates are easy to update when the rules change, provided someone owns that job. Check Consumer Affairs Victoria for when the new rules apply.</p>
<h3>SWMS</h3>
<p>Under Victoria's OHS Regulations, a Safe Work Method Statement must be prepared {L(WORKSAFE_SWMS, 'before high-risk construction work starts')}, such as work with a risk of falling more than two metres, trenches deeper than 1.5 metres, demolition or work involving asbestos. It must be kept for the duration of the work and reviewed when the work changes or after an incident.</p>
<p>AI can draft a SWMS from your templates and the job details, and flag when a change on site means one needs reviewing. The hazard assessment, and the consultation with the workers involved, stay with your people.</p>
<p>This is general information, not legal advice.</p>
"""),
("first-project", "A sensible first project", "Ask the job", """
<div class="card">
<p>Pick one live project. Give AI read-only access to its folders and the project inbox. Your supervisors and office team can then ask questions in plain English, such as "what's outstanding from the last site meeting?" or "which variations aren't signed yet?", and get answers that link to the source document.</p>
<p>It works best when job files are organised consistently, and setting that up is often half the value. Once one project works, the same setup rolls out to the next.</p>
</div>
"""),
("software", "Systems", "Works with the construction software you already run", """
<p>Software sold to Australian builders includes Buildxact, Databuild and Procore, and Simpro is built for trade contractors. Buildxact covers estimating, variations and invoicing for residential builders, and Procore is aimed at head contractors and subcontractors. AI connects these to your email, folders and accounts rather than replacing them.</p>
"""),
],
"faqs": [
("variation-notice", "Can AI write a variation notice?",
 f"""<p>It can draft one from site notes in seconds, with the description, price and change to the completion date. For domestic work the variation generally has to be {L(CAV_VARIATIONS, 'agreed in writing before the work is done')}, so the builder checks the draft and the owner signs it first.</p>"""),
("sop-claims-ai", "Can AI prepare our security of payment claims?",
 f"""<p>Yes, as drafts. AI can prepare each month's claim from your job data with the {L(SOP_CLAIM, 'required wording')} and keep a register of claims you receive, with the 10-business-day deadline for each payment schedule. Check every claim and schedule before it's served. This is general information, not legal advice.</p>"""),
("swms-changes", "Can AI keep our SWMS up to date when the work changes?",
 f"""<p>It can flag when it should happen. If site notes or a variation show the work has changed, AI can mark the affected SWMS for review and draft the changes. {L(WORKSAFE_SWMS, 'WorkSafe Victoria')} requires a SWMS to be reviewed when the work changes, and the review itself needs the people who know the site.</p>"""),
("job-folders", "Can AI find things across our job folders and emails?",
 """<p>Yes, and it's often the biggest win for builders. With read-only access to a project's folders and inbox, AI can answer questions and link to the drawing, RFI or email the answer came from. It works much better when files are named and filed consistently.</p>"""),
("construction-cost", "What does it cost to start using AI in a construction business?",
 """<p>Workshop AI's Claude for Owners starts at A$1,500 and Claude for Business at A$2,500, both fixed price. Discovery, which maps how the business really runs before anything is built, is A$3,600. Custom builds start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project. All prices exclude GST.</p>"""),
],
},

# ============================================================== Logistics
{
"slug": "ai-for-logistics",
"short": "Logistics and transport",
"audience": "logistics, freight, transport and warehousing businesses",
"title": "AI for logistics and transport businesses, Melbourne | Workshop AI",
"description": ("How freight, transport and warehousing businesses use AI for booking emails, proof of "
                "delivery and invoice checks, surcharge capture, customer updates and Chain of "
                "Responsibility records."),
"eyebrow": "AI for logistics and transport",
"h1": "AI for logistics and transport businesses",
"lede": ("In transport and logistics, AI is strongest on the paperwork and messages around the freight: "
         "booking requests from email, proof of delivery checks against invoices, surcharges that never "
         "get billed, customer updates, and the records you need for Chain of Responsibility. Routing and "
         "dispatch decisions are better left to dedicated software and your people."),
"sections": [
("where-time-goes", "Where the time goes", "Five office jobs AI handles well in logistics", f"""
<ul>
<li><strong>Bookings from email.</strong> Booking requests arrive as emails, spreadsheets and PDFs. AI reads them, sets up the booking in your transport management system for a person to confirm, and asks the customer for anything missing.</li>
<li><strong>Proof of delivery against invoices.</strong> AI checks that every delivered job has a POD attached and that the invoice matches what was delivered, then lists the exceptions for a person to chase.</li>
<li><strong>Surcharges.</strong> Waiting time, detention, tail lifts, futile pick-ups and redeliveries are {L(CARIO_SURCHARGES, 'common freight surcharges')}, and they're easy to miss. AI can read driver notes and POD comments and flag jobs where a surcharge should have been billed.</li>
<li><strong>Customer updates.</strong> Same-day changes, delays and failed deliveries mean a stream of messages. AI drafts them from the job status in your tone, and a person sends or approves.</li>
<li><strong>Reporting.</strong> Late and failed deliveries by customer, lane and reason, written up in plain English each week rather than assembled by hand.</li>
</ul>
"""),
("cor", "Chain of Responsibility", "Records AI can keep in order", f"""
<p>The Heavy Vehicle National Law {L(NTC_HVNL, 'applies in Victoria')}, and the amended law {L(NHVR_LAW, 'started on 1 August 2026')}, including updated fatigue rules and simpler work diary record-keeping. Under Chain of Responsibility, parties such as employers, operators, schedulers, consignors, loaders and unloaders each have a {L(NHVR_PRIMARY, 'primary duty')} to ensure the safety of their transport activities so far as is reasonably practicable. That duty can't be handed to anyone else, including software.</p>
<p>What AI can do is keep the records behind it complete. Fatigue records, such as work diaries for work 100 kilometres or more from base and local records such as daily run sheets, must be {L(NHVR_RECORDS, 'kept for three years')}, and the NHVR expects all work records to be {L(NHVR_FALSE, 'truthful, factual and complete')}. AI can check run sheets and records for gaps and inconsistencies every day and list them for a person to resolve.</p>
<p>For dangerous goods, the {L(ADG_VIC, 'ADG Code applies in Victoria')} under regulations administered by WorkSafe Victoria. AI can check transport documents against your checklist before the load leaves. It doesn't replace your dangerous goods training or your responsibility.</p>
<p>This is general information, not legal advice.</p>
"""),
("first-project", "A sensible first project", "Find the unbilled surcharges", """
<div class="card">
<p>Run AI across the last three months of completed jobs, PODs and driver notes, and list every job where waiting time, a tail lift, a futile pick-up or a redelivery was recorded but not invoiced. Then run the same check every week.</p>
<p>It uses data you already have, and the answer is a dollar figure, which makes it a fair test of whether AI deserves more of your time.</p>
</div>
"""),
("software", "Systems", "Works with the transport software you already run", """
<p>Systems sold to Australian transport and logistics businesses include CartonCloud, MachShip, Transvirtual and Teletrac Navman, usually alongside Xero or MYOB for accounts. AI reads from and writes to these where they allow it, and connects them to the inboxes where the work actually arrives.</p>
<p>Based in the west? Workshop AI is in Hobsons Bay, next to the western freight precincts. See <a href="/ai-in-melbournes-west/">AI help in Melbourne's west</a>.</p>
"""),
],
"faqs": [
("route-planning", "Can AI plan our routes?",
 """<p>That's usually a job for dedicated routing and dispatch software, which is built for it. AI is more useful around it: reading bookings in, updating customers, checking PODs and reporting on what went wrong.</p>"""),
("bookings-into-tms", "Can AI read booking emails into our transport management system?",
 """<p>If your system has an API or an import, usually yes. AI reads the email or attachment, builds the booking and a person confirms it. Start with one customer's bookings, measure the accuracy, then widen it.</p>"""),
("cor-ai", "Can AI help with Chain of Responsibility?",
 f"""<p>It can help with the records, not the duty. AI can check fatigue records and run sheets for gaps, keep documents complete and flag inconsistencies, but the {L(NHVR_PRIMARY, 'primary duty')} stays with each party in the chain and can't be delegated.</p>"""),
("unbilled-surcharges", "Can AI find surcharges we forgot to bill?",
 """<p>Yes, and it's a good first project. AI compares driver notes and POD comments with invoices and lists jobs where waiting time, tail lifts, futile pick-ups or redeliveries were recorded but not charged.</p>"""),
("logistics-cost", "What does it cost to start using AI in a logistics business?",
 """<p>Workshop AI's Claude for Owners starts at A$1,500 and Claude for Business at A$2,500, both fixed price. Custom builds, such as a weekly surcharge check or booking reader connected to your systems, start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project. All prices exclude GST.</p>"""),
],
},

# ============================================================== Melbourne's west
{
"slug": "ai-in-melbournes-west",
"short": "Melbourne's west",
"audience": "trade, industrial and logistics businesses in Melbourne's western suburbs",
"title": "AI consultant in Melbourne's west: Hobsons Bay, Altona, Brooklyn, Derrimut | Workshop AI",
"description": ("Workshop AI is based in Hobsons Bay and works with trade, industrial and logistics "
                "businesses across Melbourne's west, from Williamstown and Altona to Brooklyn, "
                "Derrimut, Truganina and Werribee."),
"eyebrow": "Local to Melbourne's west",
"h1": "AI help for businesses in Melbourne's west",
"lede": ("Workshop AI is based in Hobsons Bay. We work with trade, industrial and logistics businesses, and "
         "meet in person anywhere across Melbourne's west, from Williamstown, Newport and Altona to Brooklyn, Derrimut, "
         "Laverton North, Truganina, Sunshine, Footscray and Werribee."),
"sections": [
("why-the-west", "Why the west", "A region built on trades, making things and moving freight", f"""
<p>The west's economy looks different from the rest of Melbourne, and so does its office work.</p>
<ul>
<li>Hobsons Bay alone has {L(ECON_HB, '8,709 local businesses and about 47,000 local jobs')}. Its largest employers are {L(ECON_HB_JOBS, 'construction, manufacturing, and transport, postal and warehousing')}, and transport, postal and warehousing employs about 11 per cent of local workers, more than twice the Victorian share.</li>
<li>The Western Industrial Precinct is {L(VIC_WIP, "one of Melbourne's largest state-significant industrial precincts")} and a centre for logistics, with major precincts at Derrimut, Brooklyn and Altona North, and Truganina emerging.</li>
<li>The {L(POM, 'Port of Melbourne')} handles more than a third of Australia's container trade, and the {L(WGT, 'West Gate Tunnel')}, open since December 2025, has changed how trucks reach it.</li>
</ul>
<p>That means a lot of businesses whose office runs on work orders, job sheets, compliance records, bookings and PODs. That's the work AI is good at.</p>
"""),
("what-we-do", "What we do here", "Hands-on, in person, close by", """
<p>Being local matters for this kind of work. The first conversation can be at your place, with the people who do the admin, or by video. Once we're working together, we sit with the office team, watch how a job moves from the first email to the final invoice, and find the steps that eat the hours.</p>
<p>From there, the work depends on the business:</p>
<ul>
<li>Trades: <a href="/ai-for-hvac/">HVAC and refrigeration</a>, <a href="/ai-for-plumbing/">plumbing and gas</a>, <a href="/ai-for-electrical/">electrical</a> and <a href="/ai-for-construction/">construction</a>.</li>
<li>Freight and warehousing: <a href="/ai-for-logistics/">logistics and transport</a>.</li>
<li>Manufacturers and wholesalers: quotes from specifications, purchase orders, supplier documents and quality records.</li>
</ul>
"""),
("suburbs", "Where we visit", "Suburbs across the west", """
<div class="table-scroll"><table class="facts">
<tr><th scope="row">Hobsons Bay</th><td>Williamstown, Newport, Spotswood, South Kingsville, Altona, Altona North, Altona Meadows, Seaholme, and parts of Laverton and Brooklyn</td></tr>
<tr><th scope="row">Wyndham</th><td>Laverton North, Truganina (shared with Melton), Point Cook, Hoppers Crossing and Werribee</td></tr>
<tr><th scope="row">Brimbank</th><td>Sunshine, Derrimut, Deer Park and Ardeer</td></tr>
<tr><th scope="row">Maribyrnong</th><td>Footscray, Yarraville, Seddon, West Footscray and Braybrook</td></tr>
</table></div>
<p>We also visit businesses anywhere else around Melbourne, and work remotely anywhere in Australia.</p>
"""),
("local-help", "Local help worth knowing", "Free and low-cost support in the west", f"""
<ul>
<li><strong>Digital Solutions.</strong> The Australian Government's {L(ASBAS, 'Digital Solutions program')}, delivered in Victoria by Melbourne Innovation Centre, offers businesses with fewer than 20 staff free workshops and up to five hours of low-cost one-to-one advice, including on AI.</li>
<li><strong>Council business programs.</strong> Hobsons Bay City Council runs {L(HB_BUSINESS, 'business workshops and events')}, which have included an introduction to AI for business. Wyndham City offers {L(WYNDHAM_IGNITE, 'free IGNITE mentoring')} for local businesses.</li>
<li><strong>LeadWest.</strong> {L(LEADWEST, 'LeadWest')} is the alliance of Brimbank, Hobsons Bay, Maribyrnong, Melton and Wyndham councils working on the region's economy.</li>
</ul>
<p>If one of these is the right first step for you, we'll say so.</p>
"""),
],
"faqs": [
("local-consultant", "Is there an AI consultant near Altona or Williamstown?",
 """<p>Yes. Workshop AI is based in Hobsons Bay, close to Altona, Williamstown, Newport and the western industrial areas, and works with trade, industrial and logistics businesses across Melbourne's west.</p>"""),
("in-person", "Do you visit businesses in person?",
 """<p>Yes. We visit businesses anywhere around Melbourne, and the west is home ground. We can meet on site, with the people who do the admin, or by video.</p>"""),
("free-help-west", "Is there free or low-cost AI help for small businesses in the west?",
 f"""<p>Some. The {L(ASBAS, 'Digital Solutions program')} offers businesses with fewer than 20 staff free workshops and up to five hours of low-cost advice, delivered in Victoria by Melbourne Innovation Centre. Local councils, including {L(HB_BUSINESS, 'Hobsons Bay')}, also run business workshops.</p>"""),
("west-businesses", "What kinds of businesses in the west does Workshop AI work with?",
 """<p>Trade, construction, industrial and logistics businesses, typically with about 10 to 30 staff, where the office work is growing faster than the team can keep up with: work orders, quotes, compliance records, bookings and invoices.</p>"""),
],
},

# ============================================================== Simpro
{
"slug": "simpro-ai",
"short": "Simpro and AI",
"audience": "trade businesses that run Simpro",
"title": "Using AI with Simpro: Claude, ChatGPT and Simpro's own AI | Workshop AI",
"description": ("Can AI read your Simpro data? Yes. A plain guide to Simpro's API, its Lightning AI, Zapier "
                "and MCP connectors for Claude and ChatGPT, what to ask once connected, and how to start "
                "safely."),
"eyebrow": "Simpro and AI",
"h1": "Using AI with Simpro",
"lede": ("Yes, AI can work with your Simpro data. Simpro has an open API, its own AI in the Lightning "
         "platform, and third-party connectors that let tools such as Claude and ChatGPT read it, and "
         "sometimes write to it. The right route depends on what you want to ask, what you want "
         "automated and what you want to spend. Here's a plain guide from a Melbourne team that has built "
         "on Simpro."),
"sections": [
("three-routes", "Three routes", "How AI connects to Simpro", f"""
<h3>1. Simpro's own AI</h3>
<p>Simpro launched {L(SIMPRO_LIGHTNING_PR, 'Lightning')} in May 2026, describing it as an AI-native operating platform. Its AI, called Cooper, comes with four agents (FieldReady, JobReady, JobScribe and JobBrief), and {L(SIMPRO_LIGHTNING, 'JustAsk')} answers plain-English questions about things like technician margins, overdue invoices and customer history. A {L(SIMPRO_RAIN_PR, 'July 2026 release')} added an AI scheduler and expanded JustAsk. At launch, Lightning was priced as an extra 15 per cent on existing contracts, rising to 25 per cent after 31 May 2026.</p>
<p><strong>Good for:</strong> questions and tasks inside Simpro, with nothing to connect. <strong>Limit:</strong> it sees Simpro, not your inbox, your accounts or your shared drive.</p>
<h3>2. Ready-made connectors</h3>
<p>{L(ZAPIER_SIMPRO, 'Zapier')} connects to Simpro with triggers such as new or updated jobs and quotes, and actions such as creating a service job or quote, and {L(ZAPIER_SIMPRO_PARTNER, 'Simpro charges nothing')} for the Zapier connection. Several services also offer MCP connectors, the standard way AI assistants such as Claude and ChatGPT use other software: {L(ZAPIER_MCP, 'Zapier MCP')}, {L(VIASOCKET_MCP, 'viaSocket')} and {L(TUGGER, 'Tugger')}, which is listed on the Simpro Marketplace and {L(TUGGER_BLOG, 'gives AI read-only access')} to a synced copy of your data.</p>
<p><strong>Good for:</strong> quick wins and simple automations. <strong>Limit:</strong> you're bound by what each connector exposes, and some connect with write access by default.</p>
<h3>3. A custom build on the API</h3>
<p>Simpro's {L(SIMPRO_API_DOCS, 'REST API')} can view, create and modify records across customers, sites, jobs, cost centres, recurring jobs, quotes, invoices, schedules, stock, purchase orders and assets, and it can send webhooks when a job changes stage. Simpro's {L(SIMPRO_PRICING, 'Australian pricing page')} lists Open API on the base plan. Simpro doesn't offer one-on-one API support, and points people to its forum or a partner.</p>
<p><strong>Good for:</strong> joining Simpro to email, Xero and documents, branded reporting, and agents that do a defined job. <strong>Limit:</strong> it needs building and looking after.</p>
"""),
("what-to-ask", "Once it's connected", "Questions worth asking your Simpro data", f"""
<ul>
<li>"What's sitting in Complete but not yet invoiced, and for how long?" Simpro's {L(SIMPRO_STAGES, 'job stages')} run Pending, Progress, Complete, Invoiced and Archived, and Complete means the work is done and waiting to be invoiced.</li>
<li>"Which quotes in Open or Progress haven't been followed up in a fortnight?" ({L(SIMPRO_QUOTES, 'Quote stages')} run Open, Progress, Complete, Approved and Closed or Archived.)</li>
<li>"Which recurring jobs fall due next month, and which maintenance customers don't have one set up?"</li>
<li>"Which cost centres on this project are running over?"</li>
<li>"Draft this month's maintenance report for this customer, in our branding."</li>
</ul>
"""),
("safely", "Start safely", "Read-only first, then earn the right to write", f"""
<ul>
<li><strong>Start read-only.</strong> Let AI look before it's allowed to change anything. Add write access one action at a time, with a person approving.</li>
<li><strong>Treat API keys like master keys.</strong> Simpro's {L(SIMPRO_AUTH, 'developer documentation')} describes an API key as a single access token that never expires. Give each integration its own credentials, limit who holds them, and remove them when they're no longer needed.</li>
<li><strong>Mind the limits.</strong> The API returns {L(SIMPRO_PAGING, 'at most 250 records per request')} and {L(SIMPRO_LIMITS, 'rejects bursts above 10 requests a second')} to one build, so well-built integrations page through data patiently.</li>
<li><strong>Keep a person on the trigger.</strong> Anything sent to a customer, any price and any job created should have a person approving it until the results have earned trust.</li>
</ul>
"""),
("example", "Client example", "Mattick Air: monthly reports from live Simpro data", """
<div class="card">
<p><strong>Mattick Air</strong> is a Melbourne commercial air conditioning business that runs Simpro. Workshop AI built branded monthly reports for Mattick Air's own customers, produced from live Simpro data, and an agent that reads every emailed work order and lands the job ready to go, with a person staying on the trigger.</p>
</div>
"""),
],
"faqs": [
("claude-connect-simpro", "Can Claude or ChatGPT connect directly to Simpro?",
 f"""<p>Yes, through a connector. Third-party MCP connectors from services such as {L(ZAPIER_MCP, 'Zapier')}, {L(VIASOCKET_MCP, 'viaSocket')} and {L(TUGGER, 'Tugger')} let Claude and ChatGPT read Simpro data, and some can also create or update records. A custom connection built on Simpro's API gives you full control over what the AI can see and do.</p>"""),
("need-lightning", "Do we need Simpro Lightning to use AI?",
 f"""<p>No. {L(SIMPRO_LIGHTNING_PR, 'Lightning')} is Simpro's own route, built in and priced as a percentage on top of your contract. Connectors and custom builds work through Simpro's API instead. Many businesses will use both: Simpro's AI inside Simpro, and a connected assistant for work that spans email, accounts and documents.</p>"""),
("official-mcp", "Is there an official Simpro MCP server?",
 """<p>We haven't found one from Simpro itself as of October 2026. The MCP connectors available come from third parties. Check what each one can read and write before you connect it.</p>"""),
("ai-create-jobs", "Can AI create jobs and quotes in Simpro?",
 f"""<p>Yes. The {L(SIMPRO_API_FAQ, 'API')} and connectors such as {L(ZAPIER_SIMPRO, 'Zapier')} can create jobs and quotes. Start with AI preparing them for a person to approve, and only let it act on its own once you trust the results.</p>"""),
("simpro-ai-cost", "What does it cost to connect AI to Simpro?",
 """<p>It depends on the route. Simpro's Lightning is priced as a percentage of your Simpro contract, ready-made connectors charge their own subscriptions or usage fees, and a custom build costs what it takes to build and run. With Workshop AI, custom builds start from A$4,400 a month on a month-to-month retainer, or can be scoped as a fixed-price project, excluding GST.</p>"""),
],
},
]


# Titles for the sources list at the foot of each page
SOURCE_TITLES = {
    ARC_RTA: "Refrigerant Trading Authorisation FAQs",
    ARC_CONDITIONS: "Conditions of authorisation",
    VIC_COOLING: "Cooling tower risk management plans: legal responsibilities",
    BPC_ESM: "Essential safety measures",
    BPC_CERTS: "Compliance certificates",
    BPC_CLASSES: "Plumber classes and categories",
    CAV_RENTAL_GAS: "Rental providers' gas and electrical safety obligations",
    YVW_BACKFLOW: "Backflow prevention testing and reporting",
    SEW_BACKFLOW: "Backflow test report form",
    VIC_ELECTRIFY: "Electric and efficiency standards for buildings",
    ESV_GAS_BPC: "Working with the Building and Plumbing Commission",
    ESV_COES: "Certificates of Electrical Safety for consumers",
    ESV_PRESCRIBED: "Prescribed and non-prescribed work",
    ESV_CONNECT: "ESVConnect Certificates of Electrical Safety",
    ESV_REC: "Registered electrical contractors",
    SOLAR_VIC: "Installer requirements",
    SOP_CLAIM: "Making a payment claim under the SOP Act",
    SOP_CHANGES: "Changes to the security of payment scheme",
    SOP_RESPOND: "Responding to a payment claim under the SOP Act",
    SOP_OVERVIEW: "Overview of security of payment",
    CAV_VARIATIONS: "Working with your building client",
    CAV_NEW_LAWS: "New domestic building contract laws passed in Victoria",
    WORKSAFE_SWMS: "Safe work method statements (SWMS)",
    NHVR_PRIMARY: "Chain of Responsibility: the primary duty",
    NHVR_LAW: "Heavy Vehicle National Law and regulations",
    NHVR_RECORDS: "Fatigue management: record-keeping requirements",
    NHVR_FALSE: "Providing false or misleading information",
    NTC_HVNL: "Heavy Vehicle National Law",
    ADG_VIC: "Australian Dangerous Goods Code (Victoria)",
    CARIO_SURCHARGES: "Hidden freight costs: where to look",
    ECON_HB: "Hobsons Bay economic profile",
    ECON_HB_JOBS: "Hobsons Bay employment by industry",
    VIC_WIP: "Western Metro Land Use Framework Plan: productivity",
    POM: "Port of Melbourne",
    WGT: "West Gate Tunnel now open",
    ASBAS: "Digital Solutions: Australian Small Business Advisory Services",
    HB_BUSINESS: "Business workshops and events",
    LEADWEST: "LeadWest",
    WYNDHAM_IGNITE: "IGNITE business mentoring",
    SIMPRO_API_FAQ: "API FAQs",
    SIMPRO_API_DOCS: "API documentation",
    SIMPRO_LIMITS: "API rate limits",
    SIMPRO_PAGING: "API pagination",
    SIMPRO_AUTH: "API authentication",
    SIMPRO_LIGHTNING_PR: "Simpro Group unveils Lightning",
    SIMPRO_LIGHTNING: "Lightning",
    SIMPRO_RAIN: "RAIN release",
    SIMPRO_RAIN_PR: "Simpro Group announces RAIN",
    SIMPRO_PRICING: "Pricing (Australia)",
    SIMPRO_STAGES: "Managing existing jobs",
    SIMPRO_QUOTES: "View quotes",
    SIMPRO_GLOSSARY: "Glossary",
    SIMPRO_ABOUT: "About us",
    ZAPIER_SIMPRO: "Simpro integrations",
    ZAPIER_SIMPRO_PARTNER: "Zapier integration partner",
    ZAPIER_MCP: "Simpro MCP",
    VIASOCKET_MCP: "Simpro MCP",
    TUGGER: "Tugger",
    TUGGER_BLOG: "How to connect Simpro to AI",
    "https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products":
        "Guidance on privacy and the use of commercially available AI products",
}
