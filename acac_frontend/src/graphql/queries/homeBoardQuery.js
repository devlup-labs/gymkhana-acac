import gql from "graphql-tag";
import { SIZES_FRAGMENT } from "../fragments/sizesFragment";
import { NEWS_FRAGMENT } from "../fragments/newsFragment";
import { EVENT_FRAGMENT } from "../fragments/eventFragment";

export const GET_BOARDS_QUERY = gql`
  query {
    boards(isActive: true) {
      edges {
        node {
          __typename
          ... on BoardNode {
            name
            slug
            cover {
              ...Sizes
            }
            pastNews {
              edges {
                node {
                  ...News
                }
              }
            }
            upcomingEvents {
              edges {
                node {
                  ...Event
                }
              }
            }
          }
        }
      }
    }
  }
  ${SIZES_FRAGMENT}
  ${NEWS_FRAGMENT}
  ${EVENT_FRAGMENT}
`;
