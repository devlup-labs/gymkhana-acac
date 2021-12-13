import gql from "graphql-tag";
import { OFFICE_BEARER_FRAGMENT } from "../fragments/officeBearerFragment";

export const GET_OFFICE_BEARERS_QUERY = gql`
  query boards {
    boards(isActive: true) {
      edges {
        node {
          name
          vicePresident {
            ...OfficeBearerFields
          }
        }
      }
    }
  }
  ${OFFICE_BEARER_FRAGMENT}
`;
