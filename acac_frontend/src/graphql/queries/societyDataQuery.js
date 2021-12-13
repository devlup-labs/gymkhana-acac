import gql from "graphql-tag";
import { SOCIETY_EVENTS_FRAGMENT } from "../fragments/eventFragment";
import { SOCIETY_NEWS_FRAGMENT } from "../fragments/newsFragment";
import { SOCIETY_DATA_FRAGMENT } from "../fragments/societyDataFragment";
import { OFFICE_BEARER_FRAGMENT } from "../fragments/officeBearerFragment";

export const GET_SOCIETY_DATA_QUERY = gql`
  query societies($slugText: String!) {
    societies(slug: $slugText) {
      edges {
        node {
          ...SocietyDataFields
          description
          resourcesLink
          cover {
            ...Sizes
          }
          studentCoordinators {
            edges {
              node {
                ...OfficeBearerFields
              }
            }
          }
          coreMembers {
            edges {
              node {
                ...OfficeBearerFields
              }
            }
          }
          ...NewsFields
          ...EventFields
          activitySet {
            edges {
              node {
                name
                description
                customHtml
              }
            }
          }
          customHtml
        }
      }
    }
  }
  ${OFFICE_BEARER_FRAGMENT}
  ${SOCIETY_EVENTS_FRAGMENT}
  ${SOCIETY_NEWS_FRAGMENT}
  ${SOCIETY_DATA_FRAGMENT}
`;
