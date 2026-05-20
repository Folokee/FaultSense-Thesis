# INSTRUCTIONS.MD
## AI Writing Assistant Guide for Master's Thesis on PV Fault Detection

---

## 1. DOCUMENT IDENTITY & CONSTRAINTS

### Document Type
- **Master's Thesis** (NOT a PFE/Engineering thesis)
- **Nature**: Comprehensive State of the Art (SOTA) review
- **Target Length**: 40-50 pages (strict upper limit - excluding references, appendices, and preliminary pages)
- **Annexes**: Maximum 10 pages if needed

### Student Context
- Final-year student at ESI (École nationale Supérieure d'Informatique)
- Specialization: Systèmes Informatiques et Logiciels (SIL)
- Internship at CDER (Centre de Développement des Énergies Renouvelables)
- **CRITICAL**: Writing language is **ENGLISH** (academic English)

---

## 2. FUNDAMENTAL WRITING PRINCIPLES

### 2.1 Core Philosophy: Simplicity and Clarity
**ALWAYS favor simplicity and clarity over complexity.**

#### Sentence Construction
- ✅ **DO**: Use short, clear, and precise sentences
- ✅ **DO**: Ensure every sentence has a verb
- ❌ **DON'T**: Use journalistic-style verbless sentences
- ❌ **DON'T**: Write overly long, convoluted sentences with multiple subordinate clauses

**Example of BAD writing:**
> "Photovoltaic systems, given their exposure to variable and unpredictable weather conditions as well as potential failures of electronic and mechanical components, thus requiring continuous monitoring."

**Example of GOOD writing:**
> "Photovoltaic systems are exposed to variable weather conditions. Their components can also experience failures. Continuous monitoring is therefore necessary."

#### Paragraph Structure
- ✅ **DO**: Create paragraphs with multiple sentences (minimum 3-4 sentences)
- ❌ **DON'T**: Create single-sentence paragraphs
- ✅ **DO**: Use paragraph indentation at the start
- ✅ **DO**: Justify all paragraphs

---

## 3. FORMATTING REQUIREMENTS

### 3.1 Typography
- **Font**: Times New Roman, 12pt for body text
- **Line Spacing**: 1.5 lines
- **Paragraph Spacing**: 6pt after each paragraph
- **Title Spacing**: 12pt before and after titles/subtitles
- **Margins**: 2.5 cm on all sides

### 3.2 Titles and Subtitles
- **Chapter titles**: Slightly larger than body (13pt)
- **Numbering system**: 
  - Chapter 1, Chapter 2, etc.
  - Subsections: 1.1, 1.2, 1.3
  - Sub-subsections: 1.1.1, 1.1.2 (maximum depth)
- ❌ **DON'T**: Underline titles
- ✅ **DO**: Use automatic formatting and numbering
- ✅ **DO**: Start each new chapter on a new page

### 3.3 What NOT to Use (Critical)
- ❌ **NO bullet points** in the main body of the thesis
- ❌ **NO numbered lists** unless absolutely essential and explicitly justified
- ❌ **NO excessive bold text** for emphasis
- ❌ **NO headers/section dividers** within paragraphs

**Exception**: Bullet points MAY be used only in:
- List of Figures
- List of Tables  
- List of Abbreviations
- References section

### 3.4 How to Present Lists in Prose
When you need to enumerate items, integrate them naturally into sentences:

**Example of BAD formatting:**
> "Faults can be classified into:
> - Electrical faults
> - Optical faults
> - Thermal faults"

**Example of GOOD formatting:**
> "Faults can be classified into three main categories: electrical faults, optical faults, and thermal faults."

Or with more detail:
> "The faults observed in PV systems include electrical faults (short circuits, defective connections), optical faults (soiling, shading), and thermal faults (hot spots, module overheating)."

---

## 4. ACADEMIC TONE & STYLE

### 4.1 Writing Voice
- ✅ **Use impersonal/passive constructions**: "It has been observed that...", "Results show that..."
- ✅ **Use third person**: "This study examines...", "The research demonstrates..."
- ❌ **Avoid first person singular**: Don't write "I found" or "I believe"
- ⚠️ **First person plural allowed sparingly**: "We focus on...", "We examine..." (when discussing methodological choices in the thesis)
- ✅ **Maintain objectivity**: Present facts, cite sources, avoid personal opinions
- ✅ **Use present tense** for established facts and literature review
- ✅ **Use past tense** only when discussing specific historical studies or completed experiments

### 4.2 Technical Precision
- ✅ **DO**: Define every technical term on first use
- ✅ **DO**: Maintain consistency in terminology throughout
- ✅ **DO**: Use standard international abbreviations (PV, ML, CNN, MPPT, etc.)
- ✅ **DO**: Spell out acronyms on first use, then use the abbreviation

**Example:**
> "Convolutional Neural Networks (CNNs) are widely used for thermal image analysis. CNNs have demonstrated high accuracy in detecting hot spots."

### 4.3 Citation Discipline
- ✅ **ALWAYS cite sources** for claims, data, methods, or findings
- ✅ **Use APA citation style**: (Author, Year) or (Author1 & Author2, Year) or (Author et al., Year)
- ✅ **Every in-text citation** must appear in the bibliography
- ✅ **Every bibliography entry** must be cited in the text
- ❌ **DON'T**: Make unsupported claims or generalizations

**Examples:**
> "The use of deep learning for PV fault detection has shown accuracy exceeding 95% in several recent studies (Karthikeyan & Jagadeeshwaran, 2024; Islam et al., 2023)."

> "According to Kurukuru et al. (2021), machine learning approaches significantly outperform traditional methods in complex fault scenarios."

---

## 5. QUALITY CONTROL CHECKLIST

### Before Submitting Any Section:

#### Language Quality
- [ ] All sentences have verbs
- [ ] No spelling or grammar errors (use spell-checker, but don't rely on it exclusively)
- [ ] No single-sentence paragraphs
- [ ] Sentences are clear and concise
- [ ] No overly complex sentence structures
- [ ] Proper use of articles (a, an, the)
- [ ] Subject-verb agreement throughout

#### Formatting Compliance
- [ ] No bullet points in body text
- [ ] No numbered lists (unless essential)
- [ ] Proper paragraph indentation
- [ ] Consistent font and spacing
- [ ] Proper title hierarchy (Chapter > Section > Subsection)

#### Academic Rigor
- [ ] All technical terms defined on first use
- [ ] All claims properly cited
- [ ] Consistent terminology throughout
- [ ] Objective, impersonal tone maintained
- [ ] Proper distinction between facts and interpretations

#### Content Structure
- [ ] Logical flow between paragraphs
- [ ] Clear transitions between ideas
- [ ] Each paragraph focuses on one main idea
- [ ] Chapter/section serves its intended purpose in the overall structure

---

## 6. SPECIFIC CONTENT GUIDELINES

### 6.1 For Literature Review Sections (Chapters 4-5)
- ✅ **DO**: Organize by themes or approaches, not chronologically by publication date
- ✅ **DO**: Synthesize findings across multiple studies
- ✅ **DO**: Identify trends, gaps, and contradictions in the literature
- ❌ **DON'T**: Simply list studies one after another ("Author X did this, Author Y did that...")
- ✅ **DO**: Critically evaluate methodologies and results

**Example of BAD literature review:**
> "Kurukuru et al. (2021) used SVMs. Islam et al. (2023) used CNNs. Karthikeyan and Jagadeeshwaran (2024) used Random Forests."

**Example of GOOD literature review:**
> "Machine learning approaches for PV fault detection are primarily distinguished by their ability to process different types of input data. Support Vector Machines (SVMs) have demonstrated effectiveness for binary fault classification using electrical data (Kurukuru et al., 2021), while Convolutional Neural Networks (CNNs) excel in analyzing thermal images and I-V curves (Islam et al., 2023). More recently, Random Forests (RFs) have been favored for their ability to handle multimodal data and their robustness against noise (Karthikeyan & Jagadeeshwaran, 2024)."

### 6.2 For Technical Explanations (Chapters 2-3)
- ✅ **DO**: Start with general concepts, then move to specific details
- ✅ **DO**: Use analogies or comparisons when helpful
- ✅ **DO**: Define the scope clearly ("In this thesis, we focus on...", "This work examines...")
- ❌ **DON'T**: Assume the reader has expert-level knowledge
- ❌ **DON'T**: Over-simplify to the point of inaccuracy

### 6.3 For Figures and Tables
- ✅ **DO**: Reference every figure/table in the text BEFORE it appears
- ✅ **DO**: Provide self-explanatory captions
- ✅ **DO**: Explain all abbreviations in the caption, even if defined in text
- ✅ **DO**: Ensure figures/tables occupy at least 1/3 of the page
- ✅ **DO**: Center figures/tables and their titles

**Example reference in text:**
> "Figure 1 presents the complete taxonomy of PV faults identified in the literature."

**Example caption:**
> "**Figure 1**: Taxonomy of faults in photovoltaic systems. PV: Photovoltaic, MPPT: Maximum Power Point Tracking, BOS: Balance of System."

### 6.4 Tables vs. Figures
- **Tables**: Contain only text and numbers. Numbered with Arabic numerals (Table 1, Table 2)
- **Figures**: Contain drawings, graphs, diagrams, images. Numbered with Arabic numerals (Figure 1, Figure 2)

---

## 7. MISTAKES TO AVOID

### 7.1 Stylistic Mistakes
❌ Using bullet points to list studies or findings  
❌ Starting sentences with "Also", "Moreover", "Furthermore" without proper integration  
❌ Overusing passive voice to the point of awkwardness  
❌ Mixing tenses inconsistently  
❌ Using informal language or colloquialisms ("lots of", "kind of", "pretty much")  
❌ Using contractions ("don't", "can't", "won't") - always use full forms in academic writing

### 7.2 Content Mistakes
❌ Providing exhaustive technical details in the introduction  
❌ Including analysis or discussion in the conclusion  
❌ Repeating the same information in multiple sections  
❌ Citing sources incorrectly or inconsistently  
❌ Making claims without evidence or citations  
❌ Using vague quantifiers without data ("many studies", "most researchers") without citations

### 7.3 Formatting Mistakes
❌ Inconsistent spacing around titles  
❌ Mixing different numbering systems  
❌ Forgetting page numbers  
❌ Improper figure/table placement (appearing before being referenced)  
❌ Using different fonts or sizes within body text  

---

## 8. SPECIAL INSTRUCTIONS FOR AI ASSISTANT

### When Writing Content:
1. **CRITICAL**: ALWAYS write in English, never in French
2. **First draft**: Focus on getting ideas and structure right, don't worry about perfect prose
3. **Revision pass**: Refine sentence structure, eliminate lists, ensure academic tone
4. **Citation check**: Verify all citations are properly formatted and included
5. **Quality control**: Apply the checklist from Section 5

### When Responding to Revision Requests:
- **Acknowledge specific issues** pointed out by the student
- **Propose concrete alternatives** rather than abstract advice
- **Maintain consistency** with previously written sections
- **Ask for clarification** if the request is ambiguous

### When Stuck or Uncertain:
- **Flag the issue** explicitly to the student
- **Propose 2-3 alternatives** for the student to choose from
- **Ask for guidance** on technical depth or specific examples
- **Don't invent citations or technical details** – admit when you need input

---

## 9. MASTER'S THESIS SPECIFIC REMINDERS

### This is a Master's Thesis (40-50 pages), NOT a PFE:
- **Focus on theoretical depth** rather than implementation details
- **Emphasize critical analysis** of the state of the art
- **Synthesize and compare** approaches systematically
- **Identify research gaps** and open challenges
- **Less technical depth** than an engineering thesis, but more analytical rigor

### Balance to Maintain:
- **Not too technical**: Avoid excessive mathematical derivations or code-level details
- **Not too superficial**: Provide sufficient depth to demonstrate mastery of the field
- **Not too descriptive**: Always analyze, synthesize, and critically evaluate
- **Not too narrow**: Cover the breadth of the field while maintaining coherence

---

## 10. FINAL QUALITY STANDARDS

### A section is ready for submission when:
1. ✅ It reads smoothly in English without awkward constructions
2. ✅ All technical terms are properly defined and consistent
3. ✅ No bullet points or numbered lists appear in body text
4. ✅ All claims are supported by citations
5. ✅ Sentences are clear, concise, and have verbs
6. ✅ Paragraphs are substantive (3+ sentences)
7. ✅ The content serves the overall thesis structure and objectives
8. ✅ Formatting complies with the charter requirements
9. ✅ The academic tone is maintained throughout
10. ✅ The section advances the reader's understanding of PV fault detection systematically

---

## 11. REFERENCE EXAMPLES

### Good Paragraph Example:
> "The integration of artificial intelligence in photovoltaic fault detection represents a major advancement over traditional methods. Classical approaches rely on physical models that require in-depth knowledge of the system and its parameters (Kurukuru et al., 2021). In contrast, machine learning methods can automatically extract discriminative features from raw data, thereby reducing dependence on human expertise. This adaptive learning capability allows systems to adjust to the specific operational conditions of each PV installation (Islam et al., 2023)."

### Good Transition Between Sections:
> "Having presented the fundamentals of photovoltaic systems and their main components, it is now appropriate to examine the different types of faults that can affect their performance. This taxonomy will provide better understanding of the methodological requirements for fault detection."

### Good Introduction to a Literature Review Subsection:
> "Deep learning methods distinguish themselves from classical approaches through their ability to learn hierarchical data representations. In the context of PV fault detection, three main architectures dominate the literature: Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and hybrid approaches combining multiple architectures."

### Good Critical Analysis Example:
> "While CNNs have demonstrated remarkable performance in image-based fault detection, achieving accuracies exceeding 95% in controlled environments (Islam et al., 2023), their effectiveness significantly degrades when deployed on real-world installations with limited or imbalanced training data (Karthikeyan & Jagadeeshwaran, 2024). This gap between laboratory performance and field deployment highlights the need for domain adaptation techniques and transfer learning approaches."

---

## 12. SPECIFIC LANGUAGE GUIDELINES FOR ENGLISH ACADEMIC WRITING

### 12.1 Proper Use of Articles
- ✅ Use "the" for specific items previously mentioned or unique entities
- ✅ Use "a/an" for non-specific singular countable nouns
- ❌ Don't use articles before plural countable nouns when speaking generally

**Examples:**
> "**The** CNN architecture presented in Figure 1..." (specific, already mentioned)
> "**A** Support Vector Machine can classify..." (general, any SVM)
> "CNNs are widely used..." (general plural, no article)

### 12.2 Active vs. Passive Voice
- ✅ Passive voice is acceptable in academic writing for objectivity
- ✅ Active voice is preferred for clarity when appropriate
- ❌ Don't overuse passive to the point of obscuring meaning

**Passive (acceptable):**
> "The model was trained on 10,000 samples."

**Active (often clearer):**
> "Researchers trained the model on 10,000 samples."

### 12.3 Transition Words and Phrases
Use these to create flow between ideas (but integrate them naturally):
- **Addition**: Furthermore, Moreover, Additionally, In addition
- **Contrast**: However, Nevertheless, Conversely, In contrast
- **Cause/Effect**: Consequently, Therefore, Thus, As a result
- **Example**: For instance, For example, Specifically
- **Summary**: In summary, Overall, In conclusion

### 12.4 ESL Mistakes to Avoid
❌ "Researches" (uncountable) → ✅ "Research" or "Studies"
❌ "Informations" (uncountable) → ✅ "Information" or "Data"
❌ "Make a research" → ✅ "Conduct research"
❌ "According to me" → ✅ "In this work" or "This thesis argues"
❌ "In the other hand" → ✅ "On the other hand"
❌ "Allows to detect" → ✅ "Allows detection of" or "Makes it possible to detect"

---

## REMEMBER: Your role is to help produce a high-quality Master's thesis that:
- Demonstrates deep understanding of PV fault detection methods
- Provides critical synthesis of the state of the art
- Maintains rigorous academic standards
- Uses clear, correct academic English
- Complies with ESI/CDER formatting requirements

**When in doubt, prioritize CLARITY and SIMPLICITY over complexity and ask for guidance**