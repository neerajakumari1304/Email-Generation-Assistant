test_cases = [
    {
        "id": 1,
        "intent": "Follow up after job interview",
        "facts": ["Attended interview on Monday", "Applied for Software Engineer role", "Interviewer was Mr. Sharma"],
        "tone": "formal",
        "reference_email": """Subject: Follow-Up on Software Engineer Interview – Monday

Dear Mr. Sharma,

I hope this message finds you well. I wanted to take a moment to thank you for the opportunity to interview for the Software Engineer position on Monday. It was a pleasure speaking with you and learning more about the role and the team.

I remain very enthusiastic about the opportunity and would love to contribute to your organization. Please let me know if you need any additional information from my end.

I look forward to hearing from you regarding the next steps.

Warm regards,
[Candidate Name]"""
    },
    {
        "id": 2,
        "intent": "Request medical leave from manager",
        "facts": ["Need 3 days leave", "Medical reason", "Work handover completed to colleague"],
        "tone": "polite",
        "reference_email": """Subject: Medical Leave Request – 3 Days

Dear [Manager Name],

I hope you are doing well. I am writing to request a medical leave of 3 days due to a health issue that requires rest and attention.

I have already completed the handover of my current tasks to my colleague to ensure there is no disruption to ongoing work during my absence.

I would be grateful for your approval and understanding. Please let me know if you need any supporting documents.

Thank you for your consideration.

Best regards,
[Your Name]"""
    },
    {
        "id": 3,
        "intent": "Apologize for missing a project deadline",
        "facts": ["Missed deadline by 2 days", "Caused by unexpected server downtime", "Will submit by tomorrow 5 PM"],
        "tone": "empathetic",
        "reference_email": """Subject: Apology for Delayed Submission

Dear [Manager Name],

I sincerely apologize for missing the project deadline by 2 days. I understand how important timely delivery is and I take full responsibility for the delay.

The primary cause was unexpected server downtime that disrupted our workflow significantly. I have since resolved the issue and the deliverable will be submitted by tomorrow at 5 PM without fail.

I assure you this will not happen again and I appreciate your patience and understanding.

Warm regards,
[Your Name]"""
    },
    {
        "id": 4,
        "intent": "Remind team about upcoming meeting",
        "facts": ["Meeting at 10 AM tomorrow", "Agenda: Q3 project progress review", "Attendance is mandatory"],
        "tone": "formal",
        "reference_email": """Subject: Mandatory Team Meeting – Tomorrow at 10 AM

Dear Team,

This is a reminder that we have a mandatory team meeting scheduled for tomorrow at 10 AM.

The agenda for this meeting will focus on the Q3 project progress review. Your attendance is required as we will be making important decisions based on the discussion.

Please ensure you come prepared with updates from your respective work areas.

Regards,
[Your Name]"""
    },
    {
        "id": 5,
        "intent": "Invite team to office celebration party",
        "facts": ["Party on Friday evening at 6 PM", "Venue is office terrace", "All team members and their families welcome"],
        "tone": "casual",
        "reference_email": """Subject: You're Invited – Team Celebration This Friday!

Hey Team!

We're throwing a celebration party this Friday evening at 6 PM up on the office terrace and you're all invited!

Feel free to bring your families along — the more the merrier! It's going to be a great evening to unwind, celebrate our recent wins, and have some fun together.

See you all there!

Cheers,
[Your Name]"""
    },
    {
        "id": 6,
        "intent": "Thank a colleague for their help on a project",
        "facts": ["Helped debug critical issue", "Worked overtime on Saturday", "Project delivered successfully to client"],
        "tone": "warm",
        "reference_email": """Subject: Thank You for Your Amazing Support!

Hi [Colleague Name],

I just wanted to take a moment to express my sincere gratitude for your help during the project. Your willingness to debug the critical issue and work overtime on Saturday made all the difference.

Because of your dedication, we were able to deliver the project successfully to the client. It truly reflects your commitment and team spirit.

Thank you again — your support means a lot!

Best,
[Your Name]"""
    },
    {
        "id": 7,
        "intent": "Follow up with client on pending proposal",
        "facts": ["Proposal sent 7 days ago", "No response received yet", "Offering a 15-minute call to discuss"],
        "tone": "formal",
        "reference_email": """Subject: Follow-Up on Proposal Submitted Last Week

Dear [Client Name],

I hope you are doing well. I am writing to follow up on the proposal we submitted 7 days ago, as we have not yet received a response.

We understand you may have a busy schedule and we are happy to schedule a brief 15-minute call at your convenience to walk you through the details and address any questions.

We look forward to the possibility of working together and hope to hear from you soon.

Kind regards,
[Your Name]"""
    },
    {
        "id": 8,
        "intent": "Send urgent reminder about project submission",
        "facts": ["Deadline is today at 5 PM", "Two team members have not submitted", "Further delay will impact client delivery"],
        "tone": "urgent",
        "reference_email": """Subject: URGENT: Project Submission Due Today by 5 PM

Dear Team,

This is an urgent reminder that the project submission deadline is today at 5 PM. As of now, two team members have not yet submitted their sections.

Please be aware that any further delay will directly impact our client delivery timeline, which is not acceptable.

Kindly submit your work immediately. If you are facing any blockers, please reach out right now so we can resolve it before the deadline.

Regards,
[Your Name]"""
    },
    {
        "id": 9,
        "intent": "Complaint about a damaged product received",
        "facts": ["Ordered product on 1st of this month", "Received damaged packaging", "Requesting replacement or full refund"],
        "tone": "formal",
        "reference_email": """Subject: Complaint Regarding Damaged Product – Order Placed on 1st

Dear Customer Support Team,

I am writing to formally raise a complaint regarding a product I ordered on the 1st of this month. Upon delivery, I found that the packaging was severely damaged, raising concerns about the condition of the product inside.

I would like to request either a replacement of the product or a full refund at the earliest convenience.

Please advise on the next steps to resolve this matter. I hope for a prompt response.

Sincerely,
[Your Name]"""
    },
    {
        "id": 10,
        "intent": "Recognize team for successful project completion",
        "facts": ["Project completed 2 days ahead of schedule", "Client gave 5-star feedback", "Team worked through tight deadlines"],
        "tone": "casual",
        "reference_email": """Subject: Huge Shoutout to the Team – We Crushed It!

Hey Everyone,

Just wanted to give a massive shoutout to the whole team — we completed the project 2 days ahead of schedule and the client gave us 5-star feedback!

This wouldn't have been possible without each one of you pushing through tight deadlines and giving your best. I'm genuinely proud of what we've accomplished together.

Let's keep this energy going. You all rock!

Cheers,
[Your Name]"""
    },
]
