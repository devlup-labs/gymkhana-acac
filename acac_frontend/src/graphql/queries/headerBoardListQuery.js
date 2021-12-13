import gql from "graphql-tag";

export const HEADER_BOARD_LIST_QUERY = gql`
  query boards {
    boards {
      edges {
        node {
          name
          slug
        }
      }
    }
  }
`;
