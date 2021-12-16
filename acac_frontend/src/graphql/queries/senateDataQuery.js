import gql from "graphql-tag";
import { OFFICE_BEARER_FRAGMENT } from "../fragments/officeBearerFragment";

export const GET_SENATE_DATA_QUERY = gql`
  query {
    senate {
      edges {
        node {
          genSecySenate {
            ...OfficeBearerFields
          }
          genSecyAcac {
            ...OfficeBearerFields
          }
        }
      }
    }
  }
  ${OFFICE_BEARER_FRAGMENT}
`;
