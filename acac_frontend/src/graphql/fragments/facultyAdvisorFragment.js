import gql from "graphql-tag";

export const FACULTY_ADVISOR_FRAGMENT = gql`
  fragment OfficeBearerFields on UserProfileNode {
    phone
    cover {
      ...Sizes
    }
    avatar {
      ...Sizes
    }
    about
    user {
      firstName
      lastName
      email
    }
    socialLinks {
      edges {
        node {
          ...SocialMedia
        }
      }
    }
  }
  ${SIZES_FRAGMENT}
  ${SOCIAL_MEDIA_ICON_FRAGMENT}
`;
