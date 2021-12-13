<template lang="pug">
v-flex(v-if="!$apollo.queries._societies.loading")
  v-parallax.topbar-style(
    dark,
    :src="society.cover.sizes.length ? society.cover.sizes.find((e) => e.name === 'full_size').url : require('../assets/home5.jpg')",
    :height="$vuetify.theme.options.parallaxHeight * 1.3"
  )
    v-layout.justify-center.align-center.fill-height
      h1 {{ society.name }}
  v-container.pa-4
    v-row.justify-center(
      :style="{ 'margin-top': `-${$vuetify.theme.options.parallaxHeight / 3.5}px` }"
    )
      v-col(sm="10", md="8")
        v-card.pa-5.elevation-8(
          :style="{ 'border-top': `8px solid ${$vuetify.theme.themes.light.primary}` }"
        )
          v-card-title.display-1.font-weight-light About
          v-card-text
            span(v-html="society.description")
          v-card-actions.justify-end(v-if="society.resourcesLink")
            | Link to resources
            v-btn.ml-2.accent(
              right,
              ripple,
              :href="society.resourcesLink",
              target="_blank"
            )
              v-icon mdi-arrow-right
  v-container
    v-layout(row)
      v-flex.md4
        v-card.background-color(flat, tile, text)
          v-card-title.headline.justify-center
            v-icon(left, large) mdi-lightbulb-outline
            | Upcoming Event
          v-card-text(v-if="society.eventSet.edges.length")
            EventTable(:eventsList="society.eventSet.edges")
          v-card-text.text-center.subtitle-1.ml-2(v-else) There are currently no events.
      v-flex.md7.offset-md1.elevation-0.pl-md-5.xs12(flat, tile, depressed)
        v-card-title.headline.justify-center
          v-icon(left, large) mdi-newspaper-plus
          | Activities and News
        v-tabs(
          fixed-tabs,
          background-color="primary lighten-1",
          dark,
          v-model="tab"
        )
          v-tab
            | Activities
          v-tab
            v-icon(left) mdi-newspaper
            | news
        v-tabs-items(v-model="tab")
          v-tab-item(v-if="society.activitySet.edges.length")
            ActivityComponent(:activitiesList="society.activitySet.edges")
          v-tab-item.pa-8.text-center.title.background-color(v-else) There are no activities.
          v-tab-item
            v-card.pa-4.background-color(flat, tile, text)
              v-card-text(v-if="society.newsSet.edges.length")
                NewsTable(:newsList="society.newsSet.edges")
              v-card-text.pa-4.title.text-center(v-else)
                | There is no news currently
  v-container.pa-8
    //- v-flex.md10.offset-md1(
    //-   v-if="society.captain || society.viceCaptainOne || society.viceCaptainTwo || society.viceCaptainThree || society.mentor"
    //- )
    //-   v-card.accent.white--text.elevation-10
    //-     v-card-title.justify-center.display-1 Key People
    //-   v-row.justify-space-around
    //-     v-flex.md4.xs12(v-if="society.captain")
    //-       CaptainComponent(
    //-         :profile="society.captain",
    //-         :designation="'Captain'"
    //-       )
    //-     v-flex.md4.xs12(v-if="society.viceCaptainOne")
    //-       CaptainComponent(
    //-         :profile="society.viceCaptainOne",
    //-         :designation="'Vice Captain'"
    //-       )
    //-     v-flex.md4.xs12(v-if="society.viceCaptainTwo")
    //-       CaptainComponent(
    //-         :profile="society.viceCaptainTwo",
    //-         :designation="'Vice Captain'"
    //-       )
    //-     v-flex.md4.xs12(v-if="society.viceCaptainThree")
    //-       CaptainComponent(
    //-         :profile="society.viceCaptainThree",
    //-         :designation="'Vice Captain'"
    //-       )
    //-     v-flex.md4.xs12(v-if="society.mentor")
    //-       CaptainComponent(:profile="society.mentor", :designation="'Mentor'")
  v-container.pa-5(v-if="society.customHtml")
    span(v-html="society.customHtml")
  v-container.pa-8(v-if="society.studentCoordinators.edges.length", fluid)
    v-flex.md8.offset-md2
      v-card.accent.white--text.elevation-10
        v-card-title.justify-center.display-1 Student Coordinators
    v-row.justify-space-around
      v-col(
        cols="12",
        md="6",
        lg="4",
        v-for="({ node }, j) in society.studentCoordinators.edges",
        :key="j"
      )
        CaptainComponent(:profile="node", :designation="'Student Coordinator'")
  v-container.pa-8(v-if="society.coreMembers.edges.length", fluid)
    v-flex.md8.offset-md2
      v-card.accent.white--text.elevation-10
        v-card-title.justify-center.display-1 Core Members
    v-row.justify-space-around
      v-col(
        cols="12",
        md="6",
        lg="4",
        v-for="({ node }, j) in society.coreMembers.edges",
        :key="j"
      )
        CoreMemberComponent(:profile="node")
</template>

<script>
import EventTable from "../components/common/tables/EventTable";
import NewsTable from "../components/common/tables/NewsTable";
import Footer from "../components/common/Footer";
import { GET_SOCIETY_DATA_QUERY } from "../graphql/queries/societyDataQuery";
import ActivityComponent from "../components/common/ActivityComponent";
import CaptainComponent from "../components/common/cards/CaptainComponent";
import CoreMemberComponent from "../components/common/cards/CoreMemberComponent";

export default {
  apollo: {
    _societies: {
      query: GET_SOCIETY_DATA_QUERY,
      variables() {
        return {
          slugText: this.$route.params.slug
        };
      },
      update: data => data.societies
    }
  },
  name: "Society",
  components: {
    CoreMemberComponent,
    CaptainComponent,
    ActivityComponent,
    Footer,
    NewsTable,
    EventTable
  },
  data: () => ({
    tab: null
  }),
  computed: {
    society() {
      return this._societies.edges[0].node;
    }
  }
};
</script>

<style scoped>
.topbar-style {
  margin-top: -48px;
}

.background-color {
  background-color: #fafafa;
}
</style>
