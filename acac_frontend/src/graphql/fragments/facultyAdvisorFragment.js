import gql from "graphql-tag";
import { SIZES_FRAGMENT } from "./sizesFragment";

export const FACULTY_ADVISOR_FRAGMENT = gql`
  fragment FacultyAdvisorFields on FacultyProfileNode {
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
