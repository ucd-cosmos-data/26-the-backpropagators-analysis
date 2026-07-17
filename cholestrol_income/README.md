# Mini Project 1: Cholesterol Screening and Income

The Backpropagators

## Introduction

This project explores whether per capita income is associated with the percentage of adults who report receiving a cholesterol screening in California counties. Access to preventive health care can vary with local economic conditions, so comparing these measures may reveal geographic patterns and disparities. This is an observational county-level analysis; it identifies association, not causation.

## Data Acquisition

**Cholesterol Screening**: County-level, age-adjusted cholesterol-screening prevalence estimates for all 58 California counties were retrieved from the CDC PLACES county dataset through its Socrata API. The analysis uses the `cholscreen_adjprev` measure.

**Per Capita Income**: Annual 2023 county-level per capita personal income and population data were obtained from California Labor Market Information. The analysis retained the Bureau of Economic Analysis per capita personal income rows.

County names and five-digit county FIPS codes were cleaned and checked before the two datasets were joined one-to-one. The resulting dataset contains 58 counties with complete values for both measures.

## EDA

Across the 58 counties, estimated cholesterol-screening prevalence ranges from 81.1% in Imperial County to 86.6% in Marin County. Per capita income ranges from $38,243 in Trinity County to $180,575 in Marin County. The county-level Pearson correlation between income and screening prevalence is 0.785, indicating a strong positive association in this dataset.

In Figure [1](https://ucd-cosmos-data.github.io/26-the-backpropagators/project/cholesterol-screening-and-income/#cholesterol-income), counties with higher per capita income generally have higher estimated cholesterol-screening prevalence. The fitted trend line summarizes this positive relationship, but the plot does not establish that income causes greater screening.

**Fig 1. Cholesterol screening prevalence vs. per capita income**

Figure [2](https://ucd-cosmos-data.github.io/26-the-backpropagators/project/cholesterol-screening-and-income/#cholesterol-choropleth) shows how estimated cholesterol-screening prevalence varies geographically. Although the overall range is fairly narrow, darker counties have higher screening estimates and lighter counties have lower estimates.

**Fig 2. Cholesterol screening prevalence by county**

Figure [3](https://ucd-cosmos-data.github.io/26-the-backpropagators/project/cholesterol-screening-and-income/#income-choropleth) shows a wider geographic contrast in per capita income. Comparing Figures 2 and 3 helps illustrate the positive county-level relationship seen in Figure 1.

**Fig 3. Per capita income by county**
