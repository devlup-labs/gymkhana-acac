import gql from "graphql-tag";
import { SIZES_FRAGMENT } from "./sizesFragment";

export const FACULTY_FRAGMENT = gql`
  fragment FacultyFields on FacultyProfileNode {
    cover {
      ...Sizes
    }
    avatar {
      ...Sizes
    }
    name
    email
    phone
  }
  ${SIZES_FRAGMENT}
`;
