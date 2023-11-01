<template lang="pug">
v-app-bar.px-md-12(app, dark, dense, v-if="!$apollo.queries.boards.loading")
  img.mr-4(:src="logo", height="40")
  v-toolbar-items(hidden-sm-and-down)
    v-btn(text, :to="{ name: 'home' }", exact)
      v-icon(:left="$vuetify.breakpoint.mdAndUp") mdi-home
      span(v-if="$vuetify.breakpoint.mdAndUp") Home
    v-menu(bottom="", offset-y, transition="slide-y-transition")
      template(v-slot:activator="{ on }")
        v-btn(text, dark, v-on="on")
          v-icon(:left="$vuetify.breakpoint.mdAndUp") mdi-account-multiple
          span(v-if="$vuetify.breakpoint.mdAndUp") Boards
          v-icon(right) mdi-chevron-down
      v-list
        v-list-item(
          v-for="({ node }, i) in boards.edges",
          :key="i",
          link,
          :to="{ name: 'board', params: { slug: node.slug } }"
        )
          v-list-item-title {{ node.name }}
    
    v-btn(text, :to="{ name: 'festivals' }")
      v-icon(:left="$vuetify.breakpoint.mdAndUp") mdi-party-popper
      span(v-if="$vuetify.breakpoint.mdAndUp") Fests
  v-spacer
</template>

<script>
import GymkhanaLogo from "../../../assets/logo.png";
import { HEADER_BOARD_LIST_QUERY } from "../../../graphql/queries/headerBoardListQuery";

export default {
  apollo: {
    boards: {
      query: HEADER_BOARD_LIST_QUERY,
    },
  },
  name: "Header",
  data: () => ({
    toolbarItems: [
      
      {
        title: "Account",
        icon: "mdi-account",
        children: [
          { title: "Profile", to: { name: "profile" } },
          { title: "Logout" },
        ],
      },
    ],
  }),
  computed: {
    logo: () => GymkhanaLogo,
  },
};
</script>

<style scoped></style>
