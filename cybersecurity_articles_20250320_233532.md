# Cybersecurity News Articles

Generated on: 2025-03-20 23:35:34

Number of collections: 2

## Collection: hackernews


## 1. YouTube Game Cheats Spread Arcane Stealer Malware to Russian-Speaking Users

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/youtube-game-cheats-spread-arcane.html  
**ID:** c61ef790584b8fbfb466085bd9b20fb8bc66915833f2c57250d2eceb18c8dd83  
**Tags:** Malware / Threat Analysis

### Content:

YouTube videos promoting game cheats are being used to deliver a previously undocumented stealer malware called Arcane likely targeting Russian-speaking users.
The unidentified threat actors behind the operation have since expanded their offerings to include a loader named ArcanaLoader that's ostensibly meant to download game cheats, but delivers the stealer malware instead. Russia, Belarus, and Kazakhstan have emerged as the primary targets of the campaign.
"But Arcane also contains an executable file of the Xaitax utility, which it uses to crack browser keys. To do this, the utility is dropped to disk and launched covertly, and the stealer obtains all the keys it needs from its console output."
"What's interesting about this particular campaign is that it illustrates how flexible cybercriminals are, always updating their tools and the methods of distributing them," Kasperksy said. "Besides, the Arcane stealer itself is fascinating because of all the different data it collects and the tricks it uses to extract the information the attackers want."
Of the two binaries, one is a cryptocurrency miner and the other is a stealer dubbed VGS that's a variant of the Phemedrone Stealer malware. As of November 2024, the attacks have been found to replace VGS with Arcane.
Adding to its capabilities, the stealer malware implements a separate method for extracting cookies from Chromium-based browsers launching a copy of the browser through a debug port.
Besides stealing login credentials, passwords, credit card data, and cookies from various Chromium- and Gecko-based browsers, Arcane is equipped to harvest comprehensive system data as well as configuration files, settings, and account information from several apps such as follows -
The batch file then utilizes PowerShell to launch two executables embedded within the newly downloaded archive, while also disabling Windows SmartScreen protections and every drive root folder to SmartScreen filter exceptions.
The attack chains involve sharing links to a password-protected archive on YouTube videos, which, when opened, unpacks a start.bat batch file that's responsible for retrieving another archive file via PowerShell.
Furthermore, Arcane is designed to take screenshots of the infected device, enumerate running processes, and list saved Wi-Fi networks and their passwords.
"What's intriguing about this malware is how much it collects," Kaspersky said in an analysis. "It grabs account information from VPN and gaming clients, and all kinds of network utilities like ngrok, Playit, Cyberduck, FileZilla, and DynDNS."
"Most browsers generate unique keys for encrypting sensitive data they store, such as logins, passwords, cookies, etc.," Kaspersky said. "Arcane uses the Data Protection API (DPAPI) to obtain these keys, which is typical of stealers."
"Although much of it was borrowed from other stealers, we could not attribute it to any of the known families," the Russian cybersecurity company noted.

---

## 2. Veeam and IBM Release Patches for High-Risk Flaws in Backup and AIX Systems

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/veeam-and-ibm-release-patches-for-high.html  
**ID:** d490bd67f6a0f853ffaedbd9a6822f447a07393e17ca1b79f52aa8c4fe6f8016  
**Tags:** Vulnerability / Software Update

### Content:

While there is no evidence that any of these critical flaws have been exploited in the wild, users are advised to move quickly to apply the necessary patches to secure against potential threats.
The development comes as IBM has shipped fixes to remediate two critical bugs in its AIX operating system that could permit command execution.
According to Bazydlo and researcher Sina Kheirkhah, CVE-2025-23120 stems from Veeam's inconsistent handling of deserialization mechanism, causing an allowlisted class that can be deserialized to pave the way for an inner deserialization that implements a blocklist-based approach to prevent deserialization of data deemed risky by the company.
Security researcher Piotr Bazydlo of watchTowr has been credited with discovering and reporting the flaw, which has been resolved in version 12.3.1 (build 12.3.1.1139).
Veeam has released security updates to address a critical security flaw impacting its Backup & Replication software that could lead to remote code execution.
The list of shortcomings, which impact AIX versions 7.2 and 7.3, is below -
"These vulnerabilities can be exploited by any user who belongs to the local users group on the Windows host of your Veeam server," the researchers said. "Better yet - if you have joined your server to the domain, these vulnerabilities can be exploited by any domain user."
This also means that a threat actor could leverage a deserialization gadget missing from the blocklist – namely, Veeam.Backup.EsxManager.xmlFrameworkDs and Veeam.Backup.Core.BackupSummary – to achieve remote code execution.
The patch introduced by Veeam adds the two gadgets to the existing blocklist, meaning the solution could once again be rendered susceptible to similar risks if other feasible deserialization gadgets are discovered.
The vulnerability, tracked as CVE-2025-23120, carries a CVSS score of 9.9 out of 10.0. It affects 12.3.0.310 and all earlier version 12 builds.
"A vulnerability allowing remote code execution (RCE) by authenticated domain users," the company said in an advisory released Wednesday.

---

## 3. The State of GRC 2025: From Cost Center to Strategic Business Driver

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.uk/grc-trends-report  
**ID:** 0a02a7082ffcdea184be9412d70dbb68b1eb1a8903a981548a0c285325e76cff  
**Tags:** Governance / Compliance

### Content:

Drata’s State of GRC 2025 report uncovers the latest trends, challenges, and opportunities shaping the GRC landscape, offering valuable insights from top industry professionals. Get the data, benchmarks, and expert perspectives you need to elevate your GRC program and position it as a strategic driver of business growth.
Fill out the form to access The State of GRC 2025 and stay ahead of the curve in risk and compliance management.
GRC is no longer just about managing risk and ensuring compliance—it’s about driving business value, building trust, and proving ROI. Organizations are evolving their GRC strategies to align with broader business objectives, leveraging automation and AI to reduce complexity and scale their programs more effectively. But despite increased budgets and awareness, many GRC teams still face mounting pressures and operational hurdles.
Despite expanded budgets and heightened executive focus, many organizations still struggle with manual processes, resource constraints, and the challenge of integrating GRC seamlessly into broader business strategies.
Traditionally viewed as cost centers, GRC programs are evolving into pivotal components of business strategy.
The integration of Artificial Intelligence (AI) into GRC processes is transforming how organizations manage compliance and risk.
Unlock Exclusive Insights into the Future of GRC
Drata is a security and compliance automation platform that continuously monitors and collects evidence of a company’s security controls, while streamlining workflows to ensure audit-readiness.
By submitting this form I agree to receive communications (including emails) from Drata. See our Privacy Notice for more info.
The latest security and compliance news, delivered.
Download the Report
© 2025 Drata Inc. All rights reserved.
Contact Sales
Key Takeaways
Solutions

---

## 4. How to Protect Your Business from Cyber Threats: Mastering the Shared Responsibility Model

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/how-to-protect-your-business-from-cyber.html  
**ID:** 9b7129a6a4b7a5cab65c429a95b456f9be382cca83ea952cd252ab16331b5547  
**Tags:** Cloud Security / Data Protection

### Content:

Cybersecurity isn't just another checkbox on your business agenda. It's a fundamental pillar of survival. As organizations increasingly migrate their operations to the cloud, understanding how to protect your digital assets becomes crucial. The shared responsibility model, exemplified through Microsoft 365's approach, offers a framework for comprehending and implementing effective cybersecurity measures.
Microsoft maintains comprehensive responsibility for securing the foundational elements of your cloud environment. Their security team manages physical infrastructure security, including state-of-the-art data centers and robust network architecture. They implement platform-level security features and regularly deploy security updates to protect against emerging threats. Your data receives protection through sophisticated encryption protocols, both during transmission and while stored. Microsoft also ensures compliance with global security standards and regulations, conducts regular security audits, and employs advanced threat detection capabilities with rapid response protocols.
In addition to these measures, a 3-2-1 backup strategy is crucial for ensuring the recovery of your organization's data in case of an incident or disaster. This involves maintaining three copies of your data (primary, secondary, and tertiary), on two different types of media (such as hard drives and tape drives), with one being offsite. Implementing a 3-2-1 backup strategy ensures that you can recover your data in the event of a disaster, reducing downtime and minimizing potential losses.
The implementation of robust authentication measures begins with enabling Security Defaults in Entra ID (formerly Azure AD). Create a pilot program starting with your IT staff to test and refine the deployment process. When configuring Multi-Factor Authentication (MFA) methods, prioritize the use of authenticator apps, Google Authenticator or Duo, over SMS for enhanced security. Develop comprehensive end-user training materials and communication plans to ensure smooth adoption.
Your MFA rollout should follow a phased approach, beginning with IT and administrative staff to build internal expertise. Next, extend implementation to department managers who can champion the change within their teams. Follow this with a controlled rollout to general staff members, and finally include external contractors in your MFA requirements.
Create a hierarchical system of sensitivity labels that reflects your organization's data handling requirements. Start with basic classifications such as Public for generally available information, and progress through Internal for company-wide data, Confidential for sensitive business information, and Highly Confidential for the most critical data assets. Implement auto-labeling policies to automatically classify common data types, reducing the burden on end users while ensuring consistent protection.
Your Data Loss Prevention (DLP) implementation should begin with enabling Microsoft 365's built-in policies that align with common regulatory requirements. Develop custom DLP policies that address your organization's specific needs, configured to monitor critical business locations including email communications, Teams conversations, and SharePoint document libraries. Create clear notification templates that explain policy violations to users and provide guidance on proper data handling.
settings to align with your organization's risk tolerance and compliance requirements. Protecting account credentials and maintaining strong password policies falls squarely within your domain. Additionally, you must actively monitor and control data sharing practices, ensure comprehensive employee security training, and determine when additional security tools are necessary to meet specific business requirements.
Think of cloud security like a well-maintained building: the property manager handles structural integrity and common areas, while tenants secure their individual units. Similarly, the shared responsibility model creates a clear division of security duties between cloud providers and their users. This partnership approach ensures comprehensive protection through clearly defined roles and responsibilities.
Configure Microsoft Defender's Safe Links feature to provide comprehensive protection against malicious URLs. Enable real-time URL scanning across all Office applications and remove the option for users to click through warnings, ensuring consistent protection. Set up Safe Links to scan URLs at the time of click, providing protection even against delayed-action threats.
For Role Based Access Control (RBAC), start by documenting your organization's existing roles and responsibilities in detail. Create role groups that align with specific job functions, beginning with Global Administrators, who should be limited to two or three trusted individuals. Define clear responsibilities for Security Administrators, Compliance Administrators, and Department-level Administrators. Implement the principle of least privilege access for each role, ensuring users have only the permissions necessary for their job functions.
Implement a structured approach to security maintenance through a weekly rotation of key tasks. The first week of each month should focus on comprehensive access reviews, ensuring appropriate permissions across all systems. Week two centers on evaluating policy effectiveness and making necessary adjustments. The third week involves detailed compliance verification against relevant standards and regulations. Complete the monthly cycle with a thorough review of security metrics and performance indicators.
Begin your security journey with a comprehensive assessment of your current security posture using Microsoft Secure Score. This evaluation will reveal existing security gaps that require immediate attention. Based on these findings, develop a detailed remediation plan with clear priorities and timelines. Establish a dedicated security governance team to oversee the implementation process and create effective communication channels for security-related updates and concerns.
Implement Safe Attachments with Dynamic Delivery to maintain productivity while ensuring document safety. Configure the system to block detected malware and extend protection across SharePoint, OneDrive, and Teams environments. Enhance your anti-phishing defenses by creating targeted protection for high-risk users such as executives and finance team members.
Begin your data protection journey by conducting a thorough assessment of your organization's information assets. Identify and categorize sensitive data types across your systems, paying particular attention to Personal Identifiable Information (PII), financial records, intellectual
Establish a comprehensive security training program that addresses different audience needs throughout the month. Begin with new employee security orientation sessions that cover fundamental security practices and company policies. Follow this with department-specific training that addresses unique security challenges and requirements for different business units. Conduct regular phishing simulation exercises to test and improve user awareness.
Organizations must maintain strong security which requires constant vigilance and adaptation. Organizations must stay informed about emerging threats and security technologies while regularly assessing and updating their security controls. Success in cybersecurity isn't measured by the absence of incidents but by the effectiveness of your detection and response capabilities.
As a Microsoft 365 user, your organization must take ownership of several critical security aspects. This includes implementing robust user access controls and choosing appropriate authentication methods for your security needs. Your team should carefully configure security
Establish a comprehensive security monitoring framework beginning with carefully calibrated alert notifications. Define clear severity thresholds that align with your incident response capabilities and ensure notifications reach the appropriate team members. Create an escalation procedure that accounts for alert severity and response time requirements.
property, and client confidential information. These classifications form the foundation of your data protection strategy.
Remember that implementing security measures is an ongoing journey rather than a destination. Regular assessment, continuous improvement, and active engagement from all stakeholders are essential for maintaining an effective security posture in today's dynamic threat landscape.
Discover how CrashPlan enhances Microsoft 365 backup and recovery here.

---

## 5. Six Governments Likely Use Israeli Paragon Spyware to Hack IM Apps and Harvest Data

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/six-governments-likely-use-israeli.html  
**ID:** 471d211f39023b90163532e7398e2a2f1ceead44b6546be2b0b71943de528b9f  
**Tags:** Spyware / Mobile Security

### Content:

The governments of Australia, Canada, Cyprus, Denmark, Israel, and Singapore are likely customers of spyware developed by Israeli company Paragon Solutions, according to a new report from The Citizen Lab.
In these attacks, targets were added to a WhatsApp group, and then sent a PDF document, which is subsequently parsed automatically to trigger the now-patched zero-day vulnerability and load the Graphite spyware. The final stage entails escaping the Android sandbox to compromise other apps on the targeted devices.
"After detecting the attacks in question, our security teams rapidly developed and deployed a fix in the initial release of iOS 18 to protect iPhone users, and sent Apple threat notifications to inform and assist users who may have been individually targeted."
"Mercenary spyware attacks like this one are extremely sophisticated, cost millions of dollars to develop, often have a short shelf life, and are used to target specific individuals because of who they are or what they do," Apple said in a statement.
The interdisciplinary lab said it identified the six governments as "suspected Paragon deployments" after mapping the server infrastructure suspected to be associated with the spyware.
"This is the latest example of why spyware companies must be held accountable for their unlawful actions," a WhatsApp spokesperson told The Hacker News at that time. "WhatsApp will continue to protect peoples' ability to communicate privately."
Evidence has also found evidence of a likely Paragon infection targeting an iPhone belonging to an Italy-based founder of the organization Refugees in Libya in June 2024. Apple has since addressed the attack vector with the release of iOS 18.
Paragon, founded in 2019 by Ehud Barak and Ehud Schneorson, is the maker of a surveillance tool called Graphite that's capable of harvesting sensitive data from instant messaging applications on a device.
Targets of these attacks included individuals spread across over two dozen countries, including several in Europe such as Belgium, Greece, Latvia, Lithuania, Austria, Cyprus, Czech Republic, Denmark, Germany, the Netherlands, Portugal, Spain, and Sweden.
The development comes nearly two months after Meta-owned WhatsApp said it notified around 90 journalists and civil society members that it said were targeted by Graphite. The attacks were disrupted in December 2024.
Further investigation of hacked Android devices has uncovered a forensic artifact dubbed BIGPRETZEL that is suspected to uniquely identify infections with Paragon' Graphite spyware.

---

## 6. Why Continuous Compliance Monitoring Is Essential For IT Managed Service Providers

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/why-continuous-compliance-monitoring-is.html  
**ID:** 9480bb082c775243beb37cd5573eb408f5da51267161cd73366dc06e59368528  
**Tags:** Data Protection / Audit Readiness

### Content:

For Managed Service Providers (MSPs), this presents a huge opportunity to expand your service offerings by providing continuous compliance monitoring—helping your clients stay compliant while strengthening their own business.
Regulatory compliance is not optional—it's a critical business necessity for SMBs. However, with millions of businesses struggling to maintain compliance, MSPs have a massive opportunity to step in with continuous compliance monitoring services.
Regulatory compliance is no longer just a concern for large enterprises. Small and mid-sized businesses (SMBs) are increasingly subject to strict data protection and security regulations, such as HIPAA, PCI-DSS, CMMC, GDPR, and the FTC Safeguards Rule. However, many SMBs struggle to maintain compliance due to limited IT resources, evolving regulatory requirements, and complex security challenges.
For MSPs, offering continuous compliance monitoring isn't just about helping existing clients—it's also a growth opportunity. Here's how compliance services can help expand your MSP business:
For many MSPs, managing compliance manually is complex, overwhelming and unprofitable. Compliance audits, documentation, and risk assessments consume valuable time and resources, often without a clear return on investment. Simply put, it's hard to sell and hard to deliver this critical service.
That's where Compliance Manager GRC comes in—helping you easily manage IT security and regulatory compliance. Think of it as a dedicated compliance copilot, ensuring businesses stay compliant with security laws and standards without the manual hassle.
Together, Compliance Monitor and Risk Manager make Compliance Manager GRC a no-brainer for MSPs looking to save time, reduce risk, and turn compliance into a high-value service.
With compliance regulations only getting stricter, MSPs that invest in continuous compliance solutions today will be well-positioned for long-term success.
For SMBs, the benefits of compliance monitoring go far beyond avoiding fines. A proactive compliance strategy can help businesses:
Compliance Monitor: Continuous Compliance Monitoring
Continuous compliance monitoring provides real-time visibility into security, data protection, and regulatory adherence. This proactive approach allows MSPs to:
By using the Compliance Monitor feature, you can save time, avoid audit headaches, and provide continuous compliance assurance to clients.
By offering proactive compliance monitoring with Compliance Manager GRC, you can:
But after implementing Compliance Manager GRC, everything changed. We streamlined compliance, focused on the right clients, and turned it into a major revenue driver—generating nearly a million dollars in professional services revenue this year alone."
"Before using Compliance Manager GRC, compliance was drowning us. One law firm client alone was costing us $5,000 a month in lost revenue and wasted time on audits and documentation. We had to walk away.
Traditional compliance audits have been conducted periodically—often annually or quarterly. However, this approach leaves gaps where security threats and compliance violations can go unnoticed.
With Compliance Manager GRC, MSPs can turn compliance into a competitive advantage, securing high-value clients and unlocking new revenue streams.
Compliance Monitor enables automated, ongoing compliance monitoring, ensuring MSPs and their clients stay compliant with minimal manual effort.
With nearly 20 million SMBs in need of compliance solutions, MSPs that provide these services are well-positioned for growth.
By implementing these strategies, you can deliver high-value compliance solutions while increasing their service revenue.
With the right tools in place, MSPs can transform compliance from a time-consuming, labor-intensive headache into a scalable, profitable service.
✅ Build long-term relationships with businesses in need of compliance expertise
To successfully offer compliance monitoring, you should:
✅ Automate compliance reporting and streamline audits
✅ Expand their service offerings and increase revenue
Risk Manager: Simplified Risk Management for MSPs
Recent data shows there are approximately 33.3 million SMBs in the U.S., and 60% or more are not fully compliant with at least one regulatory standard. That means nearly 20 million SMBs could be at risk of fines, security breaches, and reputational damage.
The Risk Manager feature helps MSPs prove their value to clients by delivering clear, actionable risk insights to support smarter decision-making.
— Javier Dugarte, VP of Sales and Operations, GoCloud Inc.
✅ Help clients avoid fines and security risks
Request a demo today.

---

## 7. CISA Adds NAKIVO Vulnerability to KEV Catalog Amid Active Exploitation

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/cisa-adds-nakivo-vulnerability-to-kev.html  
**ID:** bebe377c124b7db8fce0adf8c926f8d7b93f7ce4bf73091a19a7033049730345  
**Tags:** Cybersecurity / Vulnerability

### Content:

The vulnerability in question is CVE-2024-48248 (CVSS score: 8.6), an absolute path traversal bug that could allow an unauthenticated attacker to read files on the target host, including sensitive ones such as "/etc/shadow" via the endpoint "/c/router." It affects all versions of the software prior to version 10.11.3.86570.
The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has added a high-severity security flaw impacting NAKIVO Backup & Replication software to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.
The cybersecurity firm further noted that the unauthenticated arbitrary file read vulnerability could be weaponized to obtain all stored credentials utilized by the target NAKIVO solution and hosted on the database "product01.h2.db."
In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies are required to apply the necessary mitigations by April 9, 2025, to secure their networks.
"NAKIVO Backup and Replication contains an absolute path traversal vulnerability that enables an attacker to read arbitrary files," CISA said in an advisory.
Also added to the KEV catalog are two other flaws -
Successful exploitation of the shortcoming could allow an adversary to read sensitive data, including configuration files, backups, and credentials, which could then act as a stepping stone for further compromises.
Last week, Akamai revealed that CVE-2025-1316 is being weaponized by bad actors to target cameras with default credentials in order to deploy at least two different Mirai botnet variants since May 2024.
There are currently no details on how the vulnerability is being exploited in the wild, but the development comes after watchTowr Labs published a proof-of-concept (PoC) exploit towards the end of last month. The issue has been addressed as of November 2024 with version v11.0.0.88174.

---

## 8. Your Risk Scores Are Lying: Adversarial Exposure Validation Exposes Real Threats

**Source:** hackernews  
**Date:** 11 March 2025  
**URL:** https://thehackernews.com/2025/03/your-risk-scores-are-lying-adversarial.html  
**ID:** 2392c200e2222b73b9172f2922058661fbee9a435141c1f29af9c212890ae57a  
**Tags:** Breach Simulation / Penetration Testing

### Content:

In cybersecurity, confidence is a double-edged sword. Organizations often operate under a false sense of security, believing that patched vulnerabilities, up-to-date tools, polished dashboards, and glowing risk scores guarantee safety. The reality is a bit of a different story. In the real world, checking the right boxes doesn't equal being secure. As Sun Tzu warned, "Strategy without tactics is the slowest route to victory. Tactics without strategy is the noise before defeat." Two and a half millennia later, the concept still holds: your organization's cybersecurity defenses must be strategically validated under real-world conditions to ensure your business's very survival. Today, more than ever, you need Adversarial Exposure Validation (AEV), the essential strategy that's still missing from most security frameworks.
In many ways, relying solely on standard controls or a once-a-year test is like standing on a sturdy-seeming pier without knowing if it can withstand that hurricane when it makes landfall. . And you know the storm is coming, you just don't know when, or if your defenses are strong enough. Adversarial Exposure Validation puts these assumptions under the microscope. Not content to t just list your potential weak points, AEV relentlessly pushes against those weak points until you see which ones matter, and which ones don't. At Picus, we know that true security demands validation over faith.
Adversarial Exposure Validation (AEV) is the logical evolution for security teams ready to move beyond assumptions and wishful thinking. AEV functions as a continuous "cybersecurity stress test" for your organization and its defenses. Gartner's 2024 Hype Cycle for Security Operations consolidated BAS and automated pentesting/red teaming into the single category of Adversarial Exposure Validation, underscoring that these previously siloed tools are more powerful together. Let's take a closer look:
Crucially, AEV isn't just about technology – it's a mindset shift as well. Leading CISOs are now advocating for an "assume breach" approach: by assuming the enemy will penetrate your initial defenses, you can then focus on validating your readiness for that eventuality. In practice, this means constantly emulating adversary tactics across your full kill-chain—from initial access, to lateral movement, to data exfiltration—and ensuring your people and tools are detecting, and ideally stopping, each step. This is the goal: truly proactive defense.
One of the biggest challenges across industries for security teams is the inability to cut through the noise. This is why Adversarial Exposure Validation is so important: it refocuses your teams on what actually matters to your organization by:
At Picus, we've been at the forefront of security validation since 2013, pioneering Breach and Attack Simulation and now integrating it with automated penetration testing to help organizations really understand the effectiveness of their defenses. With the Picus Security Validation Platform, security teams get the clarity they need to act decisively. No more blind spots, no more assumptions, just real-world testing that ensures your controls are ready for today's and tomorrow's threats.
Gartner predicts that by 2028, continuous exposure validation will be accepted as an alternative to traditional pentest requirements in regulatory frameworks. Forward-thinking security leaders are already moving this way, why fortify that pier just once a year and hope for the best, when you can continually test and reinforce it to adapt to a rising tide of constantly evolving threats?
Conventional wisdom suggests that if you've patched known bugs, deployed a stack of well-regarded security tools, and passed the necessary compliance audits, you're "secure." But being in compliance isn't the same thing as actually being secure. In fact, these assumptions often create blind spots and a dangerous sense of false security. The uncomfortable truth is that CVE scores, EPSS probabilities, and compliance checklists only catalog theoretical issues, they don't actually confirm real resilience. Attackers don't care if you're proudly compliant; they care where your organization's cracks are, especially those cracks that often go unnoticed in day-to-day operations.
Ready to move from cybersecurity illusion to reality? Learn more about how AEV can transform your security program by downloading our free "Introduction to Exposure Validation" eBook.
This shift to validation-centric defense has a tangible payoff: Gartner projects that by 2026, organizations who prioritize investments based on continuous threat exposure management (including AEV) will suffer two-thirds fewer breaches. That's a massive reduction in risk, achieved by zeroing in on the right problems.
Why aren't traditional measures up to the task of assessing actual cyber exposure? Here are three main reasons.
Note: This article has been expertly written and contributed by Dr. Suleyman Ozarslan, co-founder of Picus and VP of Picus Labs, where we believe that true security is earned, not assumed.

---

## 9. CERT-UA Warns: Dark Crystal RAT Targets Ukrainian Defense via Malicious Signal Messages

**Source:** hackernews  
**Date:** 20 March 2025  
**URL:** https://thehackernews.com/2025/03/cert-ua-warns-dark-crystal-rat-targets.html  
**ID:** e124c508683b31699b0c19122f0f0afd39bbe4c57df80504b8d27dcfd8858896  
**Tags:** Cybercrime / Malware

### Content:

The activity involves distributing malicious messages via the Signal messaging app that contain supposed meeting minutes. Some of these messages are sent from previously compromised Signal accounts so as to increase the likelihood of success of the attacks.
The Computer Emergency Response Team of Ukraine (CERT-UA) is warning of a new campaign that targets the defense sectors with Dark Crystal RAT (aka DCRat).
It also comes in the wake of reports from Microsoft and Google that Russian cyber actors are increasingly focusing on gaining unauthorized access to WhatsApp and Signal accounts by taking advantage of the device linking feature, as Ukrainians have turned to Signal as an alternative to Telegram.
"With its inaction, Signal is helping Russians gather information, target our soldiers, and compromise government officials," Serhii Demediuk, the deputy secretary of Ukraine's National Security and Defense Council, said.
Signal CEO Meredith Whittaker, however, has refuted the claim, stating "we don't officially work with any gov, Ukraine or otherwise, and we never stopped. We're not sure where this came from or why."
The campaign, detected earlier this month, has been found to target both employees of enterprises of the defense-industrial complex and individual representatives of the Defense Forces of Ukraine.
The development follows Signal's alleged decision to stop responding to requests from Ukrainian law enforcement regarding Russian cyber threats, according to The Record.
CERT-UA has attributed the activity to a threat cluster it tracks as UAC-0200, which is known to be active since at least summer 2024.
"The use of popular messengers, both on mobile devices and on computers, significantly expands the attack surface, including due to the creation of uncontrolled (in the context of protection) information exchange channels," the agency added.
The reports are shared in the form of archive files, which contain a decoy PDF and an executable, a .NET-based evasive crypter named DarkTortilla that decrypts and launches the DCRat malware.
DCRat, a well-documented remote access trojan (RAT), facilitates the execution of arbitrary commands, steals valuable information, and establishes remote control over infected devices.

---

## 10. Hackers Exploit Severe PHP Flaw to Deploy Quasar RAT and XMRig Miners

**Source:** hackernews  
**Date:** 19 March 2025  
**URL:** https://thehackernews.com/2025/03/hackers-exploit-severe-php-flaw-to.html  
**ID:** 17eb581182cae6a541c385d26266f786023b7ab8f29c24d54759cec85abc4f99  
**Tags:** Threat Intelligence / Cryptojacking

### Content:

Threat actors are exploiting a severe security flaw in PHP to deliver cryptocurrency miners and remote access trojans (RATs) like Quasar RAT.
Users are advised to update their PHP installations to the latest version to safeguard against potential threats.
This unusual behavior has raised the possibility that rival cryptojacking groups are competing for control over susceptible resources and preventing them from targeting those under their control a second time. It's also consistent with historical observations about how cryptjacking attacks are known to terminate rival miner processes prior to deploying their own payloads.
About 15% of the detected exploitation attempts involve basic vulnerability checks using commands like "whoami" and "echo <test_string>." Another 15% revolve around commands used for system reconnaissance, such as process enumeration, network discovery, user and domain information, and system metadata gathering.
In perhaps something of a curious twist, the Romanian company said it also observed attempts to modify firewall configurations on vulnerable servers with an aim to block access to known malicious IPs associated with the exploit.
The vulnerability, assigned the CVE identifier CVE-2024-4577, refers to an argument injection vulnerability in PHP affecting Windows-based systems running in CGI mode that could allow remote attackers to run arbitrary code.
"Another smaller campaign involved the deployment of Nicehash miners, a platform that allows users to sell computing power for cryptocurrency," Zugec added. "The miner process was disguised as a legitimate application, such as javawindows.exe, to evade detection."
Other attacks have been found to weaponize the shortcoming of delivering remote access tools like the open-source Quasar RAT, as well as execute malicious Windows installer (MSI) files hosted on remote servers using cmd.exe.
The development comes shortly after Cisco Talos revealed details of a campaign weaponizing the PHP flaw in attacks targeting Japanese organizations since the start of the year.
Cybersecurity company Bitdefender said it has observed a surge in exploitation attempts against CVE-2024-4577 since late last year, with a significant concentration reported in Taiwan (54.65%), Hong Kong (27.06%), Brazil (16.39%), Japan (1.57%), and India (0.33%).
"Since most campaigns have been using LOTL tools, organizations should consider limiting the use of tools such as PowerShell within the environment to only privileged users such as administrators," Zugec said.
Martin Zugec, technical solutions director at Bitdefender, noted that at least roughly 5% of the detected attacks culminated in the deployment of the XMRig cryptocurrency miner.

---
## Collection: cybernews


## 11. #OnlyDown? The shocking AI scam turning disability into a fetish

**Source:** cybernews  
**Date:** 20 March 2025  
**URL:** https://cybernews.com/news/ai-deepfake-disabled-onlyfans/  
**ID:** b0fd46572c882857a2b56b120d6b0bc6c43c13790e7b747dfc255d27a0d5b2c6  
**Tags:** No Tags

### Content:

AI has gone too far. Deepfake influencers are now being used to exploit fetish markets, with fake personas designed to lure followers in and sell adult content.
Just when you thought it couldn’t get any lower, AI has hit a disgusting new rock-bottom, generating fake personas to cater to a bizarre fetish.
A woman with Down syndrome has been artificially created to pose as an Instagram influencer, with additional content on OnlyFans and Fanvue. One of the more popular fake influencers, @mariadopari, has amassed over 148,000 Instagram followers.
Although the faces of these influencers are entirely AI-generated, they are often modeled on the likenesses of real individuals whose images are stolen and deepfaked without consent.
This combination of real and artificial elements raises significant ethical questions about exploitation and consent in the digital age.
This exploitation plays on the fetishization of disabilities, even using hashtags like #onlydown to push artificial content – marking a disturbing new depth.
Recycled and stolen content is being deepfaked and reused multiple times, often linking back to the same monetized adult content pages.
The alarmingly high follower count for @mariadopari could be due to Instagram users assuming she’s a real person, with the majority having no intention of engaging with adult content.
But as is often the case, subtle glitches in facial expressions and movement give the game away.
Once again, massive ethical questions arise – why don’t platforms like Instagram and OnlyFans immediately remove this content?
Surely, pressure must mount from somewhere for stricter oversight to curb these deepfake scams and protect vulnerable communities.
As AI is being used in increasingly nasty ways, it’s worth remembering that in the last few months alone, it’s deepfaked Brad Pitt and scammed a middle-aged lady out of nearly a million dollars in a crime of the worst taste imaginable.
AI has also proclaimed Adolf Hitler’s notorious book Mein Kampf “a true work of art,” and taken crypto and money laundering to new levels.
Who knows where it’s headed next?

---

## 12. Goodbye cables, hello lasers: Alphabet’s plan to outshine Starlink

**Source:** cybernews  
**Date:** 18 March 2025  
**URL:** https://cybernews.com/news/alphabet-starlink-lasers-fibreoptics/  
**ID:** c62531d2d239eabf2046753bc5b964e5e25ae8f43f07ada4f3f8d227733d2031  
**Tags:** No Tags

### Content:

The internet’s future could be floating through the air – Alphabet’s Taara is betting on laser beams replacing traditional cables, and being a major competitor to Elon Musk’s Starlink.
Global internet infrastructure is set for a disruption as Google’s parent company Alphabet revealed that another company it owns, Taara, will be established as an independent venture, aimed at becoming a major player in the market.
Its flagship product, Taara Lightbridge, is a wireless communications system that transmits data using invisible laser beams.
Unlike traditional fibers, which take years and require high investment to install, Taara transmits data using invisible laser beams and can be set up in just a few hours.
This could be particularly advantageous in remote rural areas where fibreoptic cables are often impractical. It will also make installation cheaper.
With the demand for 5G internet ever increasing, fiber struggles to meet this growing appetite for better bandwidth.
A Taara laser beam is able to travel up to 12 miles, hopping from node to node and bypassing traditional support systems.
Taara could in effect be a maestro of innovation, potentially bridging the digital divide between urban and rural areas, where outreach had previously been bothersome.
These laser-based networks could be commercially available as soon as 2026, which is dependent on an optical phased array chip, which will feature thousands instead of hundreds of miniature light emitters, representing a weighty upgrade.
Notably, Taara’s laser tech evolved from Project Loon, Alphabet’s own initiative that used balloons floating at the edge of space.
Loon was shut down in 2021 due to the complexity of maintaining the floating balloons and its negative environmental impact – defunct balloons would end up in rural regions, on the ground like trash.
Nevertheless, the core technology of Loon remains the same, using lasers and this time without the hindrance of shifting weather patterns affecting the balloon's trajectory.
Taara represents a shift away from an experimental project into a commercially viable option, should the market demand it in the coming months and years.
Concerning urban environments, the speed of 20Gbps rivals and sometimes exceeds fiber-based cables.
The rapid deployment at which these lasers could be utilized in urban areas could be a pivotal moment, especially where scalability is concerned.
Urban growth adjusts at different quotients, and the internet framework can be adapted accordingly.
Smart cities – like Singapore or Helsinki – that leverage technology to improve the quality of life for its residents could use this flexible technology also, and a bonus could be its malleability, especially in cities prone to natural disasters.
However, Taara doesn’t come without its drawbacks. Rain, fog, and dust are known to weaken and block laser beams, so big cities will also have maintenance issues compared to fiber, which is unaffected by these conditions.
High-rise buildings, particularly skyscrapers, may also pose challenges for the deployment of such infrastructure.
The likely future will be that these laser networks will be a complementary solution to fibreoptics, as opposed to fully replacing them.
And of course, there’ll be other competitors in this space. Elon Musk's Starlink is currently the market leader in using low-orbit satellite constellations. Starlink can reach the remotest areas but the service can be expensive.
Amazon’s Project Kuiper is also expected to launch 3,200 satellites to underserved communities, with at least half of these expected to be operational by summer 2026.
The global digital divide is a trillion-dollar challenge, meaning more companies will enter the race to provide affordable, high-speed internet worldwide.

---

## 13. Algorithmic surveillance helped Amazon crush unionizing effort

**Source:** cybernews  
**Date:** 19 March 2025  
**URL:** https://cybernews.com/news/amazon-algorithmic-management-union-busting-study/  
**ID:** 878deaf28fbad08f57dc15677a5ccdba09434fe5ef227bf0a2ef406057dedbb2  
**Tags:** No Tags

### Content:

The 2021 union vote at an Amazon warehouse in Alabama ended with employees voting against unionizing. A new study says the tech giant manipulated the process using algorithmic tricks.
In April 2021, after most workers in Bessemer, Alabama, voted against joining the union, some workers told the National Labor Relations Board (NLRB) that the company had created “an atmosphere of confusion, coercion, and/or fear or reprisals” before the vote. Complaints changed nothing.
Now, in a critical study titled "Weaponizing the Workplace: How Algorithmic Management Shaped Amazon's Antiunion Campaign in Bessemer, Alabama," Teke Wiggin, a researcher at Northwestern University, says that Amazon might have pressured workers to vote in a certain way.
According to Wiggin, Amazon might have leveraged “the specific control technique of algorithmic management to repel (not just prevent) collective action by workers.”
“The findings reveal that employers can weaponize elements or effects of algorithmic management against unions via repurposing devices that algorithmically control workers, engaging in 'algorithmic slack-cutting,' and exploiting patterns of social media activity encouraged by algorithmic management,” the paper says.
What’s “algorithmic slack-cutting?” Wiggin uses the term to describe the softening of the “electronic whip” – automated, software-driven oversight.
When workers are given this proverbial carrot, they allegedly feel such a relief that they think they were awarded a benefit – even though, for example, Amazon’s Time-Off-Task tracking system is hardly respectful to the employees. That’s what happened in Bessemer.
Based on Wiggin’s interviews with 42 workers who said they worked at the Amazon warehouse in Bessemer and transcripts of hearings held by the NLRB, the report also details how Amazon used its A to Z app “to send anti-union messages to workers.”
Amazon workers use the app to clock in and out, request time off, receive company announcements, and more.
Wiggin says he was told that workers were pressured to turn on the app's notifications and then bombarded with “anti-union propaganda.”
Moreover, in Amazon’s case, scanners and computers are “constitutive elements of its algorithmic tracking and disciplinary apparatus,” adds Wiggin. Supervisors monitor workers' performance based on indicators generated by the scanners.
That’s not really news, of course. However, interviewees told Wiggin that Amazon supervisors and HR officers “weaponized” such “algorithmically assisted discipline” to further pressure workers and discourage them from voting to form a union.
As expected, an Amazon spokesperson strongly challenged the study’s findings and suggestions that the company manipulates its workers.
“Like most employers, we do expect employees to be working the majority of the time they’re clocked in, and that’s not an unreasonable expectation,” says a statement sent to The Register.
To be fair, though, Amazon has long been criticized for the quality of its working environment and treatment of its workforce. Unsurprisingly, workers of this particular corporation have attempted to form trade unions and defend their rights.
But the giant has fiercely opposed unionization drives, especially in its infamous warehouses.
In 2018, Amazon even distributed union-busting training videos, telling managers to watch out for signs of worker organization, such as employees “suddenly hanging out together” or showing interest in concepts like “living wage.”
So far, the independent Amazon Labor Union, representing some 5,500 workers in Staten Island, NY, is the only such organization of Amazon workers.
The company – which is the second largest employer in the US, employing more than 1.5 million workers across the world, has refused to recognize the union and continues to legally challenge its very existence.

---

## 14. Americans ditch doomscrolling for $130 worth of monthly streaming

**Source:** cybernews  
**Date:** 19 March 2025  
**URL:** https://cybernews.com/news/american-streaming-costs-outpace-clothing-expenditure/  
**ID:** 15e66604ddad9e69e29f7d412e54d5b0bd6ad0a60ac71728e5235e5765bf4786  
**Tags:** No Tags

### Content:

With streaming platforms now wanting you to pay for content even when they show you ads, consumers keep spending more on subscriptions. They’re not happy, a new survey shows.
The poll, commissioned by Tubi, a streaming service, found that American consumers are spending significantly more money on streaming subscriptions than the year before – $129 combined in a month on average. That’s a 7.5% increase.
Indeed, Americans are avid streamers. Thirty-eight percent of respondents said they stream for three hours or more in one sitting, and viewers are juggling nearly seven platforms. In fact, they spend more on streaming than on clothes ($109) each month.
That’s probably why 56% also said they monitor their use of streaming services carefully to avoid overspending. Gen Z viewers seem particularly cost-conscious, as 76% of them said they have or would cancel their membership if the price increased.
The findings can seem a little weird because most larger streamers began offering cheaper ad-supported plans. Shouldn’t the combined monthly sum people spend on streaming be lower?
Well, it turns out viewers don’t really like ads – or, rather, the fact that on most platforms, they still have to play even though ads interrupt their shows a few times. That’s why consumers decide to pay up and escape ads altogether.
Forty-six percent of respondents said that ads significantly disrupt their streaming experience, and 79% said: “If I’m paying for a streaming service, I expect no ads at all.”
Plus, ads sort of return the viewer to everyday struggles. This is offputting for many, with the survey finding that most people turn to streaming as a form of escapism. Eighty percent of viewers said they’d rather spend their time watching something than doomscrolling through social media.
Among the various forms of escapism at our fingertips today, consumers are most likely to reach for streaming when they need a mental break (59%) – followed by listening to music (50%) and scrolling social media (38%).
Many, especially Gen Z viewers, also use streaming as background for other daily tasks, including work, by the way. Eighty-four percent of employed Gen Z viewers say they watch TV or movies while working, and 48% say they’ve lied to co-workers or bosses about it.
What’s more, half of Gen Z (53%) say they have put off working because they had to finish a show they were binge-watching, and 52% say they don’t want to return to the office because they’ll miss streaming during the workday.

---

## 15. Britain has 10 years to prepare for encryption-breaking quantum cyberattacks

**Source:** cybernews  
**Date:** 20 March 2025  
**URL:** https://cybernews.com/news/britain-quantum-security-warning-infrastructure/  
**ID:** cba5b3ec54e35cce3bf070383f6e82b133564c3431da0819177bd679409cc28d  
**Tags:** No Tags

### Content:

As if there's not enough headache about cyberattacks already, the United Kingdom’s cybersecurity agency has urged organizations to foolproof their systems against quantum hackers by 2035.
Shoring up your digital defenses is always a good idea. Especially if attackers are well-versed in quantum-powered cyberattacks, which are not here yet but might arrive soon, the UK’s National Cyber Security Centre (NCSC) has warned in a new guidance.
According to the NCSC, large entities and operators of critical national infrastructure, such as energy and transport providers, need to introduce “post-quantum cryptography” (PQC) in order to prevent quantum tech being deployed to break into their systems.
The guidance outlines a three-phase timeline for organizations to transition to quantum-resistant encryption methods by 2035. The NCSC said: “Current encryption standards – used to protect banking, secure communications, and other sensitive data – are vulnerable to the power of quantum computers.”
These encryption methods rely on mathematical problems that current-generation computers struggle to solve. However, quantum computers have the potential to solve them much faster, which means that current encryption methods would be insecure.
The NCSC, which is part of the powerful Government Communications Headquarters (GCHQ) organization, said that migrating to PQC will help organizations stay ahead of this threat by deploying quantum-resistant algorithms before would-be attackers have the chance to exploit vulnerabilities.
Over the next three years, organizations should identify cryptographic services that need upgrades. By 2031, they should have executed high-priority upgrades, and by 2035, all security systems should have migrated to PQC.
“Our new guidance on post-quantum cryptography provides a clear roadmap for organizations to safeguard their data against these future threats, helping to ensure that today’s confidential information remains secure in years to come,” said the NCSC chief technical officer, Ollie Whitehouse.
For most small and medium-sized businesses, migrating to PQC security will be fairly routine, relying on the service of PQC specialized tech service providers. Larger organizations may have to put in place significant planning and investment, the NCSC said.
The age of quantum computing, which promises to deliver machines that are thousands of times more powerful than traditional computers, is approaching fast.
Google’s head of quantum research said last month that the company is on course to release commercial quantum computing applications within five years, challenging Nvidia's previous 20-year prediction.
Traditional computers process information one number at a time, whereas quantum computers use “qubits” that can represent several numbers at once.

---

## 16. ChatGPT just made you a criminal – with zero evidence

**Source:** cybernews  
**Date:** 20 March 2025  
**URL:** https://cybernews.com/news/chatgpt-fake-crime-hallucination/  
**ID:** d13e0a98df36162730914ea6a18611ad53b4efa711f3abd0e3f68d3b8c9088dd  
**Tags:** No Tags

### Content:

What happens when a chatbot makes up a crime – and pins it on you?
Consider the shock of finding that when you ask ChatGPT about yourself – much like when we used to Google ourselves – it falsely describes you as a child murderer.
As data protection NGO noyb has revealed, when Norwegian user Arve Hjalmar Holmen sought out information about himself, it returned a disturbing response.
At the rate technology is advancing, you’d expect better than such wild hallucinations.
This kind of delusion is far from purely a technical issue – it puts someone’s reputation and livelihood on the line.
If a screenshot like this were to go viral, the negative consequences could be severe.
There may be heavy legal consequences for OpenAI too. If found guilty, they could be penalized up to 4% of their global turnover – or €20 million, whichever is the greater sum.
Or, as in Italy in April 2023, a temporary ban may ensue – in that case, it was three weeks – all because of how ChatGPT was found to be processing personal data.
If this kind of hallucination were to happen more often – and at this stage, it’s rare – then cases of defamation or emotional distress could pile up, as well as placing an increased financial burden on the company.
Previous calamities include:
Is it enough for AI to include a disclaimer that it may be wrong? No. That’s like a Hollywood movie claiming that events are fictional and not based on real life. The difference is that ChatGPT is supposed to reflect real life – not be in the entertainment business.
The issue is currently between a rock and a hard place. OpenAI clearly can’t self-govern. Doing so would mean mass censorship, which would cripple ChatGPT, an AI that’s essentially “learning on the job.” These hallucinations aren’t intentional – they’re the result of AI conflating snippets of information.
And for governments, it’s difficult to apply swift regulation to an industry that’s moving at breakneck speed. ChatGPT toggles between "search" and "reason," and there’s a level of abstractness to these differentiations.
Right now, it seems like a string of isolated incidents. But if this kind of foul play were to multiply, societal mistrust in AI would skyrocket.

---

## 17. Chinese satellites “dogfighting” in space, US Space Force says

**Source:** cybernews  
**Date:** 20 March 2025  
**URL:** https://cybernews.com/news/chinese-satellites-practicing-combat-maneuvers/  
**ID:** 1dc3dcd452bde33b088ef2bbf5042cf7b8acb0fe40e3eb493116a7f7012c2b59  
**Tags:** No Tags

### Content:

China is becoming increasingly aggressive in space and is now practicing coordinated satellite maneuvers that look a lot like classic aerial combat, a US Space Force General has said. He warns that America needs to be prepared for an off-planet conflict.
Speaking at the McAleese Defense Programs Conference in Washington, the vice chief of space operations, General Michael Guetlein, said that China has been aggressively developing capabilities in space and that this is a threat to American superiority.
That’s not really anything new, as China has never hidden its ambitions in space. In 2025 alone, the country is reportedly targeting around 100 orbital launches, and in January, it launched a refueling station in geosynchronous equatorial orbit to service its satellite fleet.
Improved capabilities for maintaining and prolonging the operational lifespan of satellites already in orbit can reduce costs and improve sustainability in space operations.
But there’s more, Guetlein said. Quite obviously, on-orbit satellite refueling might be useful for both peacetime and wartime scenarios, and, according to the general, there are clear signs China is preparing for the possibility of off-planet warfare.
"We observed five objects in space moving in and out and around each other in synchrony and in control. That's what we call dogfighting in space – they are practicing tactics, techniques, and procedures to do in-orbit space operations from one satellite to another,” Guetlein said.
Commercial satellites first spotted the maneuvers – that looked like offensive drills – and relayed the information to the US Space Force.
Guetlein didn’t explicitly say that these were Chinese satellites – but a Space Force spokesperson later confirmed it in an email sent to reporters.
“Gen. Guetlein referenced Chinese satellite maneuvers observed in space. China conducted a series of proximity operations in 2024 involving three Shiyan-24C experimental satellites and two Chinese experimental space objects, the Shijian-6 05A/B. These maneuvers were observed in low Earth orbit. These observations are based on commercially available information,” the spokesperson said.
“Dogfighting” between satellites in space would, of course, be very different and much slower than our imagination would want it to be. The laws of physics mean that any kind of space war would take days if not weeks.
However, the use of this well-known term highlights the need for the Space Force to improve its capabilities and maintain space superiority in any future conflict.
According to Guetlein, China already has a large fleet of active signal jammers in space. It’s also spoofing traffic and generally behaving much more aggressively.
“Unfortunately, our current adversaries are willing to go against international norms of behavior, and they’re willing to do it in very unsafe and unprofessional manners,” said the general.
“The new norms of behavior in space are jamming, spoofing, and dazzling. Cyber hacks are happening around us on a daily basis. What’s more concerning is the new kit they’re bringing to space. The environment has completely changed.”
Guetlein said that there used to be a capability gap between America and its “near peers,” mainly driven by the United States' technological advancement. That capability gap is now significantly narrowing and may soon reverse.

---

## 18. Digital activists oppose US bill protecting children online: why?

**Source:** cybernews  
**Date:** 12 March 2025  
**URL:** https://cybernews.com/news/electronic-frontier-foundation-child-protection-bill/  
**ID:** c59e9aa2c59e5291bca79dd1116efa0a7032c697ce898e7888623925716d3281  
**Tags:** No Tags

### Content:

The Electronic Frontier Foundation (EFF), a prominent digital rights group, has once again expressed its opposition to a bill intended to protect children from online sexual exploitation. Activists say it’s quite simple: the document does no such thing.
The bipartisan “Strengthening Transparency and Obligation to Protect Children Suffering from Abuse and Mistreatment Act” of 2023 (the STOP CSAM Act) is slowly advancing in the US Senate.
According to senators sponsoring the bill, social media is full of child sexual abuse material while the big tech companies do too little and have to be held accountable.
Proponents of the bill are urging the Senate Committee on the Judiciary to quickly pass it because, currently, as Republican Senator Josh Hawley says, the victims have no legal recourse against the firms allowing CSAM to proliferate on their platforms.
The STOP CSAM bill makes it a crime to “promote or facilitate” the sexual exploitation of children. The bill also opens the door for civil lawsuits against providers for the negligent “promotion or facilitation” of conduct relating to child exploitation.
However, digital rights organizations are adamant: the bill actually reduces safety online. According to the EFF, while the goal to protect children is important and laudable, “laudable goals do not always make good law.”
The initiative itself seems demonstrative because existing laws already require online service providers to report CSAM to the National Center for Missing and Exploited Children. Then, actionable reports are forwarded to law enforcement agencies.
The new bill, the EFF says, creates a “convoluted” notice-and-takedown regime overseen by a new Child Online Protection board, where providers may be required to remove lawful content prior to any adjudication that the content is in fact CSAM.
“This system is ripe to be gamed by bad actors, leaving lawful user content exposed to bogus takedown requests,” the EFF points out, adding that the bill threatens the privacy, security, and free expression of all users, including children.
The organization also sees a threat to end-to-end encryption and says that it’s “unfortunate” that government agencies, including the FBI, keep pushing the idea that strong encryption can be coupled with easy access by law enforcement.
Hackers from Salt Typhoon, a China-backed group, breached US telecom systems last year by infiltrating the same systems that the major providers had opened to US law enforcement and intelligence agencies.
“If there’s any upside to a terrible breach like Salt Typhoon, it’s that it is waking up some officials to understand that encryption is vital to both individual and national security. In fact, in response to this breach, a top US cybersecurity chief said that encryption is your friend,” said the EFF.

---

## 19. Anti-Elon crusades in US and Europe make Tesla their main target

**Source:** cybernews  
**Date:** 14 March 2025  
**URL:** https://cybernews.com/news/elon-musk-protests-target-tesla/  
**ID:** 536955239ebab60fad6933721fb90e6fe72acb9a8e7efae7dcde900dc4dfe67a  
**Tags:** No Tags

### Content:

People have had enough of Elon Musk. Americans are protesting DOGE cuts by vandalizing Teslas, while Europeans denounce Musk’s support of far-right parties by posting Nazi ads across London.
In the US, Americans are done with Musk's brutal cuts as a part of his Department of Government Efficiency (DOGE) reform.
Americans who own Musk’s vehicles are desperately trying to blend into the crowd by disguising their Tesla cars as Toyota, Honda, or Mazda vehicles.
A few cars were spotted in Seattle using badges of different car brands to avoid backlash.
Tesla owners in California and across the country are disguising their vehicles to avoid vandalism and protest Musk’s sweeping governmental cuts affecting USAID and hundreds of thousands of jobs nationwide.
In Oregon, a Tesla dealership was shot at for a second time following ongoing vandalism and protests against the Tesla CEO, ABC news reports.
In Washington, Tesla Cybertrucks were spray painted with red swastikas and Musk’s name, implying that Musk is a Nazi.
Cybertrucks covered in the words “Fuck Elon” were spotted in a parking lot. The post said that roughly 30 Cybertrucks had been vandalized. However, the exact number is not known.
Back in Seattle, a man bought a Tesla just to destroy it in protest of Musk’s companies.
President Donald Trump suggested that vandalism of Tesla vehicles, dealerships, and other property relating to the electric vehicle company will be seen as domestic terrorism.
Trump said that protesters are “harming a great American company,” the BBC reports, and that anyone who is caught showing violence towards Tesla will “go through hell.”
While Musk’s DOGE reforms have impacted the American population, across the pond, Europeans are protesting Musk for different reasons.
Musk’s unwavering support for right-wing political parties, his lack of support for Ukraine, and his outright critique of the European way of life leave a bitter taste in the mouths of many Europeans.
So much so that Tesla has become a target, French media reports the destruction of Tesla vehicles outside a French dealership, similar to attacks in the United States.
Far-left activists called “Volcano Group” claimed responsibility for an arson attack on the Tesla Berlin Gigafactory that left the factory without power and halted operations. An action that was dubbed by Musk as “extremely dumb.”
According to Reuters, climate activists in London have poured orange liquid latex over Tesla's humanoid robot in protest of Musk.
One guerilla ad for Tesla reads: “Goes from 0 to 1939 in 3 seconds – Tesla the Swasticar.”
Another ad on the London Underground shows Musk displaying the Nazi hand symbol. The fake ad is for a product called “Elon’s Musk,” a perfume with a swastika on the bottle.
Tesla’s shares dropped 15% on Monday (March 10th), the biggest one-day drop in five years, while its market capitalization has dropped 45% since hitting a record $1.5 trillion on December 17th.
Following the Tesla sell-off, Trump blamed the “radical left lunatics” for attempting to “illegally and collusively boycott Tesla, one of the world’s great automakers, and Elon’s ’baby.”
Tesla sales in the EU and the UK fell by half in January. Sales have also been falling in California, the company’s biggest market in the United States.

---

## 20. World’s “biggest” Elon Musk protest staged in Wales

**Source:** cybernews  
**Date:** 18 March 2025  
**URL:** https://cybernews.com/news/elon-musk-tesla-protest-wales/  
**ID:** f194ccc723c848bf5733c1fcffdc23a19c558497d8ddbbdc5ae96d829b4e40b9  
**Tags:** No Tags

### Content:

"Don’t buy a Tesla" was raked into the sand by protesters on a Welsh beach alongside a silhouette of Elon Musk giving a Nazi salute.
A message calling for a Tesla boycott appeared on Black Rock Sands, a popular beach in northern Wales, as part of a stunt by the UK-based protest group Led By Donkeys.
“Thousands of people are ditching Tesla. Here’s one of them with a message you can see from space,” the group said on social media, including posts on Bluesky and X.
Musk, who owns both Tesla and X, has recently become a target of protests – mainly in the US, where he is spearheading President Donald Trump’s controversial cost-cutting measures, and in Europe, where he has expressed support for far-right movements.
The billionaire has been accused of making a “Heil Hitler” salute during Trump’s inauguration event in January, an allegation he has denied.
The message was raked into the sand by Tesla driver Prama, who is selling her Model 3 after six years in protest of “Musk’s embrace of the global far-right.” In a video shared by Led By Donkeys, she can be seen creating the image using a harrow attached to her car.
The image reportedly measures 250m x 150m.
“We used to joke that Elon Musk is a real-life Iron Man, but then there’s so many things that have happened,” Prama says in the clip. “He's gone into becoming someone who is obsessed by power, and that's really changed my view on him.”
“And when he started getting onto the tickets of the extreme far-right, that's when I started thinking, 'I'm not really sure I should be driving a Tesla.’”
According to Prama, the “absolute pinnacle” for her decision was the infamous salute, from which she said was “no turning back.”
“My message to anyone who’s thinking about buying a Tesla – don’t. Don’t put your money towards this extremism and division of society. Please, don’t buy a Tesla,” she concludes, echoing the message raked into the sand.
In January, Led By Donkeys and a German protest group Politische Schönheit, or Political Beauty, claimed they projected images of Musk performing a raised-armed salute, accompanied by the word “Heil,” onto the outside of Tesla’s plant in Berlin. An investigation has been opened by the police.
Led By Donkeys was founded as an anti-Brexit protest group in 2018 and has since staged numerous protests against right-wing politicians in the UK. Its recent stunts have also included demonstrations in support of Ukraine and Palestine.
In addition to peaceful anti-Musk protests, including a guerilla ad campaign in London targeting the billionaire, a number of violent attacks on Tesla cars and showrooms across the US and Europe have been reported in recent weeks.
Eight Teslas were torched outside a dealership in Toulouse, in southern France, earlier this month, while at least four Teslas were set on fire in Berlin last week. In the UK, around 20 cars were damaged in an attack on a Tesla dealership in Belfast just yesterday.
Similar attacks were reported in the US, with Tesla cars vandalized in Oregon, Washington, and Massachusetts, among other places.
Tesla sales have been tanking ever since Musk took on a more active political role, with the automaker hit particularly hard in Germany, where sales dropped by 76% in February.
The billionaire faced widespread criticism for what was seen as an attempt to influence Germany’s federal election last month when he threw his support behind the far-right AfD party.
Tesla sales were down 55% in Italy, 53% in Portugal, 48% in Norway and Denmark, 45% in France, and 24% in the Netherlands. In the UK, sales were up 21% despite the backlash against Musk, following a 12% slump in January.
Outside Europe, Tesla sales in Australia were down 72% in February compared to the same month in 2024, while Tesla registrations in the US fell 11% year over year in January.
President Trump blamed the “radical left lunatics” for attempting to “illegally and collusively boycott Tesla,” which he called “Elon’s baby.”

---
