
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meridian Forward | HCM AS2",
    page_icon="📘",
    layout="wide"
)


# ---------- DESIGN ----------
st.markdown("""
<style>
.stApp {
    background-color: #f7f9fb !important;
    color: #23313c !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #f7f9fb !important;
}
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stWidgetLabel"] p,
label {
    color: #23313c !important;
}
h1, h2, h3 {
    color: #15364f !important;
}
div[data-testid="stMetric"] {
    background: white !important;
    border: 1px solid #dce5e9;
    padding: 16px;
    border-radius: 12px;
}
.red-note {
    color: #c62828 !important;
    background: #fff0f0;
    border-left: 5px solid #c62828;
    padding: 12px;
    border-radius: 5px;
}
.small-note {
    color: #667780 !important;
}
</style>
""", unsafe_allow_html=True)


# ---------- SIDEBAR ----------
st.sidebar.title("Meridian Forward")
st.sidebar.caption("HCM AS2 | Team 02")
section = st.sidebar.radio(
    "Navigate portfolio",
    [
        "1. Business Alignment",
        "2. Workforce Planning",
        "3. Recruitment & Onboarding",
        "4. E-Portfolio & Reflection",
        "5. Mentor Engagement"
    ]
)
st.sidebar.divider()
st.sidebar.info(
    "This portfolio separates case inputs from proposed decisions "
    "and assumptions."
)

# ---------- HEADER ----------
st.title("Meridian Forward")
st.subheader("Aligning People with Strategy")
st.caption(
    "Human Capital Management | Assessment 2 | Team 02"
)
st.divider()

# ---------- SECTION 1 ----------
if section == "1. Business Alignment":
    st.header("01 | Business Alignment and the SHRBP Mandate")

    left, right = st.columns(2)
    with left:
        st.markdown("### Business challenge")
        st.write(
            "Move toward shorter product cycles and more original "
            "design while keeping existing services reliable."
        )
    with right:
        st.markdown("### People problem")
        st.write(
            "Responsibility is moving faster than decision authority. "
            "Skills, handoffs and approval delays can slow delivery."
        )

    st.markdown("### From business need to decision")
   
st.markdown("""
<div style="display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px;">
  <div style="background:white; border:1px solid #dce5e9; border-radius:12px; padding:20px;">
    <p style="color:#667780; margin:0;">01</p>
    <h3 style="color:#15364f; margin:8px 0;">Business need</h3>
    <p style="color:#23313c; margin:0;">Shorter product cycles and original design.</p>
  </div>
  <div style="background:white; border:1px solid #dce5e9; border-radius:12px; padding:20px;">
    <p style="color:#667780; margin:0;">02</p>
    <h3 style="color:#15364f; margin:8px 0;">Capability gap</h3>
    <p style="color:#23313c; margin:0;">Skills, handoffs and decision authority.</p>
  </div>
  <div style="background:white; border:1px solid #dce5e9; border-radius:12px; padding:20px;">
    <p style="color:#667780; margin:0;">03</p>
    <h3 style="color:#15364f; margin:8px 0;">Workforce decision</h3>
    <p style="color:#23313c; margin:0;">Allocate capacity and close specialist gaps.</p>
  </div>
  <div style="background:white; border:1px solid #dce5e9; border-radius:12px; padding:20px;">
    <p style="color:#667780; margin:0;">04</p>
    <h3 style="color:#15364f; margin:8px 0;">Business outcome</h3>
    <p style="color:#23313c; margin:0;">Faster delivery with reliable existing services.</p>
  </div>
</div>
""", unsafe_allow_html=True)


    st.markdown("### Who does what?")
    st.dataframe(
        pd.DataFrame({
            "Role": [
                "Business leaders",
                "SHRBP",
                "Line managers",
                "HR specialists"
            ],
            "Responsibility": [
                "Set priorities and retain high-risk decisions",
                "Align people strategy with business goals",
                "Manage release of staff and service coverage",
                "Support recruitment, learning and workforce evidence"
            ]
        }),
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "Recommendation: test selective decentralisation. "
        "Delegate defined, low-risk decisions while retaining "
        "authorised controls over pricing, customer consent and "
        "major architecture exceptions."
    )

# ---------- SECTION 2 ----------
elif section == "2. Workforce Planning":
    st.header("02 | Work Design and Workforce Planning")
    st.write(
        "Four-week pilot | Proposed bounded delegation | "
        "Role-specific capacity"
    )

    st.markdown("### Q5.02: How productive hours are calculated")
    st.latex(r"40 \times 4 = 160 \text{ contracted hours}")
    st.latex(r"160 \times 80\% = 128 \text{ productive hours}")
    st.write(
        "Existing fixed service commitments must then be deducted "
        "to calculate the hours available for pilot work."
    )

    roles = pd.DataFrame({
        "Role": [
            "Engineering", "Analytics", "Operations",
            "Data Preparation", "Quality Assurance", "Legacy Experts"
        ],
        "Employees": [20, 12, 8, 6, 6, 8],
        "Available hours": [640, 576, 256, 192, 192, 128],
        "Pilot demand hours": [560, 368, 212, 272, 264, 192]
    })
    roles["Balance (hours)"] = (
        roles["Available hours"] - roles["Pilot demand hours"]
    )

    capacity = int(roles["Available hours"].sum())
    demand = int(roles["Pilot demand hours"].sum())
    balance = capacity - demand
    role_gaps = int(
        roles.loc[roles["Balance (hours)"] < 0, "Balance (hours)"]
        .sum() * -1
    )

    x, y, z = st.columns(3)
    x.metric("Available capacity", f"{capacity:,} h")
    y.metric("Proposed pilot demand", f"{demand:,} h")
    z.metric("Overall balance", f"{balance:+,} h")

    st.markdown("### Capacity by role")
    st.dataframe(roles, use_container_width=True, hide_index=True)

    st.markdown("### Role-specific shortages")
    gaps = roles[roles["Balance (hours)"] < 0][
        ["Role", "Balance (hours)"]
    ].copy()
    gaps["Shortage (hours)"] = gaps["Balance (hours)"].abs()
    gaps = gaps.drop(columns=["Balance (hours)"])
    st.dataframe(gaps, use_container_width=True, hide_index=True)

    st.warning(
        "The overall balance is a surplus of 116 hours, but specialist "
        "roles still have a combined shortage of 216 hours. Surplus "
        "hours in one role cannot automatically replace another role's skills."
    )

    st.markdown("### Conditional vendor option")
    vendors = pd.DataFrame({
        "Role": ["Data Preparation", "Quality Assurance", "Legacy Experts"],
        "Shortage hours": [80, 72, 64],
        "Estimated vendor cost": ["₹88,000", "₹1,28,000", "₹1,60,000"]
    })
    st.dataframe(vendors, use_container_width=True, hide_index=True)
    st.metric("Estimated total vendor cost", "₹3,76,000")
    st.caption(
        "Conditional on the proposed coordination reductions and "
        "confirmation that duplicate customer-pack work can be removed."
    )

    st.markdown("### Planning constraints")
    st.write("- Vendor workers provide 102.4 effective role-hours each.")
    st.write("- The four-week vendor budget is ₹6,00,000.")
    st.write("- The maximum is eight vendor workers.")
    st.write("- Permanent hires take eight weeks to start.")
    st.write("- Existing legacy work cannot be removed without owner approval.")

    st.markdown(
        '<div class="red-note"><b>VERIFY BEFORE SUBMISSION:</b> '
        'Confirm the bounded-delegation assumptions and the single '
        'authoritative customer-pack output and receiving owner.</div>',
        unsafe_allow_html=True
    )

# ---------- SECTION 3 ----------
elif section == "3. Recruitment & Onboarding":
    st.header("03 | Recruitment, Selection and Onboarding")
    st.write("Fill confirmed skill gaps, not simply increase headcount.")

    a, b, c = st.columns(3)
    with a:
        st.markdown("### 1. Internal first")
        st.write(
            "Identify existing employees with the required skills. "
            "Protect pilot time and arrange service coverage."
        )
    with b:
        st.markdown("### 2. Targeted vendors")
        st.write(
            "Consider role-specific vendors for confirmed specialist "
            "shortages, within the approved budget."
        )
    with c:
        st.markdown("### 3. Fair selection")
        st.write(
            "Use consistent job-related criteria and work samples. "
            "Document decisions and check for bias."
        )

    st.divider()
    st.markdown("### Onboarding checklist")
    onboarding = [
        "Prepare approved system and data access.",
        "Explain role expectations and escalation rules.",
        "Assign a named internal owner or buddy.",
        "Start with supervised tasks and feedback.",
        "Document knowledge transfer.",
        "Check quality and permissions before independent work."
    ]
    for item in onboarding:
        st.checkbox(item, key="onboard_" + item)

    st.warning(
        "Permanent external hires take eight weeks to start, so they "
        "add no capacity during this four-week pilot."
    )

# ---------- SECTION 4 ----------
elif section == "4. E-Portfolio & Reflection":
    st.header("04 | E-Portfolio: Evidence of Our Work")
    st.write(
        "This section records the evidence, assumptions, revisions "
        "and learning behind our recommendation."
    )

    st.markdown("### Evidence to include")
    st.write("- Case diagnosis and application of Mintzberg's framework.")
    st.write("- Workforce calculations and assumptions.")
    st.write("- Sources used and decisions made.")
    st.write("- Genuine team contributions and dated evidence.")
    st.write("- Revisions made after feedback.")
    st.write("- AI-use note, following faculty instructions.")

    st.markdown("### Reflection")
    reflection = st.text_area(
        "What did your team learn from this case?",
        placeholder=(
            "Write your own reflection: what you learned, "
            "what changed in your thinking, and why."
        ),
        height=150
    )

    st.markdown("### Evidence links")
    portfolio_url = st.text_input(
        "Portfolio or supporting evidence URL",
        placeholder="Paste your actual link here"
    )
    evidence_notes = st.text_area(
        "Evidence description",
        placeholder="Describe the actual file, screenshot or contribution."
    )

    st.markdown(
        '<div class="red-note"><b>COMPLETE BEFORE SUBMISSION:</b> '
        'Add the working portfolio URL, dated evidence, individual '
        'contributions and your AI-use note. Do not claim work is '
        'completed unless it is genuinely completed.</div>',
        unsafe_allow_html=True
    )

# ---------- SECTION 5 ----------
elif section == "5. Mentor Engagement":
    st.header("05 | Corporate Mentor Engagement and Accountability")

    st.markdown("### Proposed mentor question")
    st.info(
        "For this pilot, which low-risk technical decisions can India "
        "resolve locally, and what evidence should trigger escalation?"
    )

    st.markdown("### Record actual engagement")
    mentor_date = st.text_input(
        "Date of engagement",
        placeholder="Enter the actual date"
    )
    mentor_format = st.selectbox(
        "Engagement status",
        ["Not yet recorded", "Planned", "In progress", "Completed"]
    )
    mentor_attendees = st.text_input(
        "Attendees",
        placeholder="Enter actual attendees"
    )
    mentor_guidance = st.text_area(
        "Guidance received",
        placeholder="Record the mentor's actual key points.",
        height=120
    )
    mentor_response = st.text_area(
        "Our response",
        placeholder="Explain what the team adopted, adapted or declined, and why.",
        height=120
    )

    st.markdown("### Safeguards")
    st.write("- Protect existing service commitments.")
    st.write("- Retain authorised controls over pricing and customer consent.")
    st.write("- Keep major architecture exceptions with authorised owners.")
    st.write("- Narrow or defer the pilot if skills, hours or budget do not hold.")

    st.markdown(
        '<div class="red-note"><b>IMPORTANT:</b> Enter only real mentor '
        'details and feedback. If no engagement has happened, leave it '
        'as planned or not yet recorded.</div>',
        unsafe_allow_html=True
    )

# ---------- FOOTER ----------
st.divider()
st.caption(
    "Meridian Forward | HCM AS2 | Team 02 — "
    "Case inputs, calculations and proposed decisions should be "
    "clearly distinguished."
)
