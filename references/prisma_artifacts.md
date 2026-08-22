# PRISMA-ScR artifacts

Track at least:

- records identified by each source;
- records imported;
- automatic duplicates removed;
- manual duplicates removed;
- records screened;
- records excluded at title/abstract;
- reports sought for retrieval;
- reports not retrieved;
- full texts assessed;
- full texts excluded by primary reason;
- studies/documents included.

Use one primary exclusion reason per record. Suggested controlled values:

`wrong_domain`, `wrong_policy_object`, `wrong_population_or_context`,
`conceptual_or_theoretical`, `social_innovation_only`, `health_technology_assessment_only`,
`not_empirical`, `no_full_text`, `duplicate`, `wrong_document_type`, `other`.

Counts must be reproducible from the row-level files. Never manually change a
PRISMA total without documenting the source rows and the reason for change.

