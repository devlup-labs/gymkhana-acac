<template lang="pug">
  div(v-if="!$apollo.queries._boards.loading")
    v-parallax(
      :src="board.cover.sizes.find(e => e.name === 'full_size').url").board-photo.text-center
      v-overlay(absolute)
        p(class="white--text").display-2 {{ board.name }}
    v-container
      v-row.ma-4
        v-col(cols="12" md="8")
          v-card(flat tile text color="#fafafa" )
            v-card-title.headline About
            v-card-text.subtitle-1
              blockquote.blockquote.ma-2(class="black--text")
                p “Every child is an artist, the problem is staying an artist when you grow up.”
                p -   Pablo Picasso
            span(v-html="board.description")
            v-row.mt-6
              v-btn.elevation-4(class="accent mr-4" :href="board.reportLink" target="_blank") Annual Report
                v-icon(right) mdi-arrow-right
              v-btn.elevation-4(class="accent mr-4" :href="board.constitutionLink" target="_blank") Constitution
                v-icon(right) mdi-arrow-right
        v-col(cols="12" md="4")
          v-card(flat tile text color="#fafafa")
            v-card-title.headline.justify-center
              v-icon(left) mdi-pen
              | Upcoming Event
            v-card-text(v-if="board.upcomingEvents.edges.length")
              EventTable(:eventsList="board.upcomingEvents.edges")
            v-card-text(v-else).subtitle-1.text-center.ml-4 There are no upcoming events.
    v-row(class="grey lighten-3").pa-5
      v-col(cols="12" md="8" offset-md="2")
        v-card(class="accent white--text")
          v-card-title.display-1.justify-center Societies
      v-container(v-if="board.societySet.edges.length").md12
        v-row.pa-3.justify-space-around
          v-col(cols="12" md="4" v-for="({ node }, n) in board.societySet.edges" :key="n")
            StripedCard(:node="node")
      v-container(v-else).md12.pa-5.title.text-center
            | There are currently no societies in the board.
    v-row.pa-5.justify-center
      v-col(cols="12" sm="10" md="6" lg="4")
        v-card(flat tile text color="#fafafa" )
          v-card-title.headline.justify-center
            v-icon(left) mdi-newspaper
            | News
          v-card-text(v-if="board.pastNews.edges.length")
            NewsTable(:newsList="board.pastNews.edges")
          v-card-text(v-else).title.text-center
            | There is no news for the current Board.
    v-row(class="grey lighten-3" v-if="board.president || board.vicePresident").pa-5
      v-col(cols="12" md="8" offset-md="2")
        v-card(class="accent white--text")
          v-card-title.display-1.justify-center Key People
      v-col(cols="12")
        v-container
          v-row.justify-space-around
            v-col(cols="12" md="4" v-if="board.president")
              FacultyCard(:avatarSize="120" :profile="board.president" :designation="'President'" )
            v-col(cols="12" md="4" v-if="board.vicePresident")
              OfficeBearerCard(:avatarSize="120" :profile="board.vicePresident" :designation="'Vice President'")
            
</template>

<script>
import Footer from "../components/common/Footer";
import EventTable from "../components/common/tables/EventTable";
import OfficeBearerCard from "../components/OfficeBearerCard";
import FacultyCard from "../components/FacultyCard";
import NewsTable from "../components/common/tables/NewsTable";
import { GET_BOARD_DATA_QUERY } from "../graphql/queries/boardDataQuery";
import StripedCard from "../components/common/cards/StripedCard";

export default {
  apollo: {
    _boards: {
      query: GET_BOARD_DATA_QUERY,
      variables() {
        return {
          slugText: this.$route.params.slug
        };
      },
      update: data => data.boards
    }
  },
  name: "Board",
  components: {
    StripedCard,
    NewsTable,
    OfficeBearerCard,
    FacultyCard,
    EventTable,
    Footer
  },
  computed: {
    board() {
      return this._boards.edges[0].node;
    }
  }
};
</script>

<style scoped>
.board-photo {
  margin-top: -48px;
  height: 30rem !important;
  background-size: cover !important;
  -webkit-background-size: cover !important;
}
.v-application .blockquote {
  border-left: 0.3rem solid #4791db;
}
.stripe {
  background-color: rgba(255, 255, 255, 0.74);
}
</style>
