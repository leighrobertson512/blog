Title: [Enterprise] Architecture 
Date: 2014-10-03
Category: Notes
Status: draft
Tags: architecture, enterprise architecture, technical standards
Author: Wray
Summary: Defining/Choosing the appropriate Software Architecture Standard Taxonomy/Ontology

In my flashback effort to leverage web logging to capture activities that will be useful to myself (and perhaps others) in the future, I'll document the thought process we followed in defining the Enterprise Architecture standards Hierarchy/Taxonomy/Ontology.

First off, in this specific environment, there exists some previous work following the TOGAF which has a very nice organization of artifacts to supplement their framework. Also, in this environment, the FEAF framework has been tossed around as another potential basis for organization. And efforts have been done to take existing artifacts and try to map them into both of these frameworks. Furthermore, as is the case in most large organizations, there is an SOA effort underway that should be considered as part of all of this.

So, we have been asked to come up with a taxonomy that can be used in this specific environment to classify a few existing standards, standards that we will create as part of this effort and, of course, standards that will be created in the future.

Initially the TOGAF seemed logical and made sense with respect to other taxonomies I've used and helped customize in the past. However, the client has mentioned a desire not to be so "functional" and spending more time looking at the FEAF, I see the advantages for that approach.

Furthermore, I was on a previous project here where we defined more of an ontology than a taxonomy for the lower-level application developer standards. Thus, we can sort of take a multi-pronged approach to arrive at a site-specific taxonomy:

inputs:

high level
  -TOGAF
  -FEAF
  -Forrester overview of EA
  -Previous work 

site-level
  -App Dev Ontology
  -CMDBI aspects (attributes) of CIs
  -Existing standards
  -organizational layout (mostly to ensure taxonomy is agnostic to the organization)
  -Personal Previous work (e.g. concept that a standard is a mature/approved decision -- lifecycle of the standards).
