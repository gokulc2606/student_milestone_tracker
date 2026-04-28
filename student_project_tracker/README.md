# Student Project & Milestone Tracker

## SOFTWARE REQUIREMENTS SPECIFICATION (SRS)

**Project:** Departmental ERP Mini-Modules | **Stack:** Django 4+, Python, SQLite, jQuery/AJAX

### 1. Project Components, Requirements & Syllabus Mapping

| Component    | Requirement | Syllabus Mapping |
| -------- | ------- |------- |
| Architecture | MVT Pattern, Loose Coupling, URL Routing | Module 1, CO1 |
| Database | SQLite (dev), ORM Models, FK/M2M Relations | Module 2, CO2 |
| Frontend | Template Inheritance, Generic Views, jQuery/AJAX | Modules 2,3,5, CO3/CO5 |
| Admin | Customized Django Admin for CRUD & Workflow | Module 3, CO2 |
| Exports | `HttpResponse` with `text/csv` & `application/pdf` MIME types | Module 4, CO4 |

---

## CO-SDG Mapping

| COURSE OUTCOME | HOW THIS PROJECT DEMONSTRATES IT | SDG TARGET ADDRESSED |
| -------- | ------- |------- |
| CO1: MVT Architecture | URL routing for registration, upload, export endpoints | SDG 4.4 (Skills for employment) |
| CO2: Models & Forms | Project/Milestone models + validated file upload forms | SDG 9.5 (Research capacity) |
| CO3: Template Inheritance | Reusable base.html + guide/student dashboard views | SDG 4.5 (Equitable access) |
| CO4: Non-HTML Output | CSV export with MIME type + filtered querysets | SDG 16.6 (Effective institutions) |
| CO5: AJAX Integration | (Bonus) Real-time title validation without page refresh | SDG 9.5 (Innovation infrastructure) |

---

## SDG Justification

"Our Student Project & Milestone Tracker advances SDG 4: Quality Education (Target 4.4) by digitizing capstone project management — enabling students to develop industry-aligned software engineering practices through structured milestone tracking. The CSV export feature (CO4) supports SDG 16 (Target 16.6) by providing transparent, filterable progress reports for faculty coordinators. Built with Django's MVT architecture (CO1) and validated forms (CO2), the system ensures equitable access (SDG 4.5) for all student teams regardless of technical background, while optional AJAX title search (CO5) demonstrates responsive, user-centered design aligned with modern web standards."
