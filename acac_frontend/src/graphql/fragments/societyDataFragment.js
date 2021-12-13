import gql from "graphql-tag";

export const SOCIETY_DATA_FRAGMENT = gql`
  fragment SocietyDataFields on SocietyNode {
    name
    slug
  }
`;
