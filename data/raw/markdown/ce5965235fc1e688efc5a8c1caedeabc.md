![ACL Logo](https://aclanthology.org/images/acl-logo.svg) ACL Anthology ⟨1⟩
  * About⟨2⟩
    * Announcements⟨3⟩
    * Communication channels⟨4⟩
    * Related work⟨5⟩
    * Copyright⟨6⟩
    * * * *
    * Credits⟨7⟩
    * Volunteer⟨8⟩
    * Development⟨9⟩
    * Feedback⟨10⟩
  * Using⟨2⟩
    * Citing papers⟨11⟩
    * Links in the Anthology⟨12⟩
    * Data access⟨13⟩
    * * * *
    * All FAQs⟨14⟩
    * * * *
    * ###### Details
    * Anthology identifiers⟨15⟩
    * Names⟨16⟩
    * ORCID iDs⟨17⟩
    * DOIs⟨18⟩
    * Verified authors⟨19⟩
  * Contributions⟨2⟩
    * Submissions⟨20⟩
    * Corrections⟨21⟩
    * Author pages⟨22⟩
    * Attachments⟨23⟩
  * GitHub⟨24⟩


## Word-level Translation Quality Estimation Based on Optimal Transport⟨25⟩
Yuto Kuroda⟨26⟩, Atsushi Fujita⟨27⟩, Tomoyuki Kajiwara⟨28⟩
##### Correct Metadata for 
Use this form to create a GitHub issue with structured data describing the correction. You will need a GitHub account. Once you create that issue, the correction will be reviewed by a staff member.
⚠️ Mobile Users: Submitting this form to create a new issue will only work with github.com, not the GitHub Mobile app.
**Important** : The Anthology treat PDFs as authoritative. Please use this form only to correct data that is out of line with the PDF. See our corrections guidelines⟨21⟩ if you need to change the PDF.
Title Adjust the title. Retain tags such as <fixed-case>.
Authors Adjust author names and order to match the PDF.Add Author
Abstract Correct abstract if needed. Retain XML formatting tags such as <tex-math>. You may use <b>...</b> for **bold** , <i>...</i> for _italic_ , <u>...</u> for _underline_ , <sc>...</sc> for small-caps, <tt>...<tt> for `typewriter text`, <url>...</url> for URLs, <a href=...> for hyperlinks, and <par/> for paragraph breaks.
Verification against PDF Ensure that the new title/authors match the snapshot below. (If there is no snapshot or it is too small, consult the PDF⟨2⟩.)
![](https://aclanthology.org/2024.amta-research.18/)⟨2⟩
Authors concatenated from the text boxes above:
ALL author names match the snapshot above—including middle initials, hyphens, and accents.
Create GitHub issue for staff review
* * *
##### Abstract
Word-level translation quality estimation (TQE) is the task of identifying erroneous words in a translation with respect to the source. State-of-the-art methods for TQE exploit large quantities of synthetic training data generated from bilingual parallel corpora, where pseudo-quality labels are determined by comparing two independent translations for the same source text, i.e., an output from a machine translation (MT) system and a reference translation in the parallel corpora. However, this process is sorely reliant on the surface forms of words, with acceptable synonyms and interchangeable word orderings regarded as erroneous. This can potentially mislead the pre-training of models. In this paper, we describe a method that integrates a degree of uncertainty in labeling the words in synthetic training data for TQE. To estimate the extent to which each word in the MT output is likely to be correct or erroneous with respect to the reference translation, we propose to use the concept of optimal transport (OT), which exploits contextual word embeddings. Empirical experiments using a public benchmarking dataset for word-level TQE demonstrate that pre-training TQE models with the pseudo-quality labels determined by OT produces better predictions of the word-level quality labels determined by manual post-editing than doing so with surface-based pseudo-quality labels. 

Anthology ID:
    2024.amta-research.18 

Volume:
    Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)⟨29⟩ 

Month:
    September 

Year:
    2024 

Address:
    Chicago, USA 

Editors:
     Rebecca Knowles⟨30⟩, Akiko Eriguchi⟨31⟩, Shivali Goel⟨32⟩ 

Venue:
    AMTA⟨33⟩ 

SIG:


Publisher:
    Association for Machine Translation in the Americas 

Note:


Pages:
    209–224 

Language:


URL:
    <https://aclanthology.org/2024.amta-research.18/> 

DOI:


Bibkey:
    kuroda-etal-2024-word 

Cite (ACL):
    Yuto Kuroda, Atsushi Fujita, and Tomoyuki Kajiwara. 2024. Word-level Translation Quality Estimation Based on Optimal Transport⟨34⟩. In _Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)_ , pages 209–224, Chicago, USA. Association for Machine Translation in the Americas. 

Cite (Informal):
    Word-level Translation Quality Estimation Based on Optimal Transport⟨34⟩ (Kuroda et al., AMTA 2024) 

Copy Citation:
     BibTeX Markdown MODS XML Endnote More options… 

PDF:
    <https://aclanthology.org/2024.amta-research.18.pdf>
PDF ⟨25⟩Cite ⟨2⟩Search ⟨35⟩ Fix data⟨2⟩
* * *
##### Export citation
  * BibTeX⟨36⟩
  * MODS XML⟨37⟩
  * Endnote⟨38⟩
  * Preformatted⟨39⟩



```
@inproceedings{kuroda-etal-2024-word,
    title = "Word-level Translation Quality Estimation Based on Optimal Transport",
    author = "Kuroda, Yuto  and
      Fujita, Atsushi  and
      Kajiwara, Tomoyuki",
    editor = "Knowles, Rebecca  and
      Eriguchi, Akiko  and
      Goel, Shivali",
    booktitle = "Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)",
    month = sep,
    year = "2024",
    address = "Chicago, USA",
    publisher = "Association for Machine Translation in the Americas",
    url = "https://aclanthology.org/2024.amta-research.18/",
    pages = "209--224",
    abstract = "Word-level translation quality estimation (TQE) is the task of identifying erroneous words in a translation with respect to the source. State-of-the-art methods for TQE exploit large quantities of synthetic training data generated from bilingual parallel corpora, where pseudo-quality labels are determined by comparing two independent translations for the same source text, i.e., an output from a machine translation (MT) system and a reference translation in the parallel corpora. However, this process is sorely reliant on the surface forms of words, with acceptable synonyms and interchangeable word orderings regarded as erroneous. This can potentially mislead the pre-training of models. In this paper, we describe a method that integrates a degree of uncertainty in labeling the words in synthetic training data for TQE. To estimate the extent to which each word in the MT output is likely to be correct or erroneous with respect to the reference translation, we propose to use the concept of optimal transport (OT), which exploits contextual word embeddings. Empirical experiments using a public benchmarking dataset for word-level TQE demonstrate that pre-training TQE models with the pseudo-quality labels determined by OT produces better predictions of the word-level quality labels determined by manual post-editing than doing so with surface-based pseudo-quality labels."
}
```

Download as File Copy to Clipboard

```
<?xml version="1.0" encoding="UTF-8"?>
<modsCollection xmlns="http://www.loc.gov/mods/v3">
<mods ID="kuroda-etal-2024-word">
    <titleInfo>
        <title>Word-level Translation Quality Estimation Based on Optimal Transport</title>
    </titleInfo>
    <name type="personal">
        <namePart type="given">Yuto</namePart>
        <namePart type="family">Kuroda</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Atsushi</namePart>
        <namePart type="family">Fujita</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <name type="personal">
        <namePart type="given">Tomoyuki</namePart>
        <namePart type="family">Kajiwara</namePart>
        <role>
            <roleTerm authority="marcrelator" type="text">author</roleTerm>
        </role>
    </name>
    <originInfo>
        <dateIssued>2024-09</dateIssued>
    </originInfo>
    <typeOfResource>text</typeOfResource>
    <relatedItem type="host">
        <titleInfo>
            <title>Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)</title>
        </titleInfo>
        <name type="personal">
            <namePart type="given">Rebecca</namePart>
            <namePart type="family">Knowles</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <name type="personal">
            <namePart type="given">Akiko</namePart>
            <namePart type="family">Eriguchi</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <name type="personal">
            <namePart type="given">Shivali</namePart>
            <namePart type="family">Goel</namePart>
            <role>
                <roleTerm authority="marcrelator" type="text">editor</roleTerm>
            </role>
        </name>
        <originInfo>
            <publisher>Association for Machine Translation in the Americas</publisher>
            <place>
                <placeTerm type="text">Chicago, USA</placeTerm>
            </place>
        </originInfo>
        <genre authority="marcgt">conference publication</genre>
    </relatedItem>
    <abstract>Word-level translation quality estimation (TQE) is the task of identifying erroneous words in a translation with respect to the source. State-of-the-art methods for TQE exploit large quantities of synthetic training data generated from bilingual parallel corpora, where pseudo-quality labels are determined by comparing two independent translations for the same source text, i.e., an output from a machine translation (MT) system and a reference translation in the parallel corpora. However, this process is sorely reliant on the surface forms of words, with acceptable synonyms and interchangeable word orderings regarded as erroneous. This can potentially mislead the pre-training of models. In this paper, we describe a method that integrates a degree of uncertainty in labeling the words in synthetic training data for TQE. To estimate the extent to which each word in the MT output is likely to be correct or erroneous with respect to the reference translation, we propose to use the concept of optimal transport (OT), which exploits contextual word embeddings. Empirical experiments using a public benchmarking dataset for word-level TQE demonstrate that pre-training TQE models with the pseudo-quality labels determined by OT produces better predictions of the word-level quality labels determined by manual post-editing than doing so with surface-based pseudo-quality labels.</abstract>
    <identifier type="citekey">kuroda-etal-2024-word</identifier>
    <location>
        <url>https://aclanthology.org/2024.amta-research.18/</url>
    </location>
    <part>
        <date>2024-09</date>
        <extent unit="page">
            <start>209</start>
            <end>224</end>
        </extent>
    </part>
</mods>
</modsCollection>

```

Download as File Copy to Clipboard

```
%0 Conference Proceedings
%T Word-level Translation Quality Estimation Based on Optimal Transport
%A Kuroda, Yuto
%A Fujita, Atsushi
%A Kajiwara, Tomoyuki
%Y Knowles, Rebecca
%Y Eriguchi, Akiko
%Y Goel, Shivali
%S Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)
%D 2024
%8 September
%I Association for Machine Translation in the Americas
%C Chicago, USA
%F kuroda-etal-2024-word
%X Word-level translation quality estimation (TQE) is the task of identifying erroneous words in a translation with respect to the source. State-of-the-art methods for TQE exploit large quantities of synthetic training data generated from bilingual parallel corpora, where pseudo-quality labels are determined by comparing two independent translations for the same source text, i.e., an output from a machine translation (MT) system and a reference translation in the parallel corpora. However, this process is sorely reliant on the surface forms of words, with acceptable synonyms and interchangeable word orderings regarded as erroneous. This can potentially mislead the pre-training of models. In this paper, we describe a method that integrates a degree of uncertainty in labeling the words in synthetic training data for TQE. To estimate the extent to which each word in the MT output is likely to be correct or erroneous with respect to the reference translation, we propose to use the concept of optimal transport (OT), which exploits contextual word embeddings. Empirical experiments using a public benchmarking dataset for word-level TQE demonstrate that pre-training TQE models with the pseudo-quality labels determined by OT produces better predictions of the word-level quality labels determined by manual post-editing than doing so with surface-based pseudo-quality labels.
%U https://aclanthology.org/2024.amta-research.18/
%P 209-224
```

Download as File Copy to Clipboard
##### Markdown (Informal)
Word-level Translation Quality Estimation Based on Optimal Transport⟨34⟩ (Kuroda et al., AMTA 2024)
  * Word-level Translation Quality Estimation Based on Optimal Transport⟨34⟩ (Kuroda et al., AMTA 2024)


##### ACL
  * Yuto Kuroda, Atsushi Fujita, and Tomoyuki Kajiwara. 2024. Word-level Translation Quality Estimation Based on Optimal Transport⟨34⟩. In _Proceedings of the 16th Conference of the Association for Machine Translation in the Americas (Volume 1: Research Track)_ , pages 209–224, Chicago, USA. Association for Machine Translation in the Americas.


Copy Markdown to Clipboard Copy ACL to Clipboard
![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)⟨40⟩ ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License⟨41⟩. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License⟨42⟩.
The ACL Anthology is managed and built by the ACL Anthology team⟨7⟩ of volunteers.
_Site last built on 22 July 2026 at 14:46 UTC withcommit 280e4ed⟨43⟩._
