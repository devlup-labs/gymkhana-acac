<template lang="pug">
  div
    v-carousel(
      v-if="!$apollo.queries.homeCarousel.loading && homeCarousel"
      :height="carouselHeight"
      v-resize="onResize"
      elevate-on-scroll
      cycle
      hide-delimiter-background
      show-arrows-on-hover
    ).topbar-margin
      v-carousel-item(
        v-for="({node}, i) in homeCarousel.photos.edges"
        :key="i"
        :src="node.image.sizes[0].url"
        transition="fade-transition"
        reverse-transition="fade-transition"
      )
        v-layout.display-1.mask.justify-center.align-center.fill-height
          v-layout(
            column
            transition="fade-transition"
          ).white--text.text-center.font-weight-light.topbar-margin
            v-flex Students' Gymkhana
            v-flex IIT Jodhpur
    v-container.pa-10
      v-row
        v-col
          h1.mb-2.display-1.text-center About Students' Gymkhana
          v-row.justify-center
            v-col(md="6" align-self="center")
              p.subtitle-1.text-center  Students' Gymkhana, IIT Jodhpur is the governing body that looks after all student activities.
      v-row(v-if="!$apollo.queries.boards.loading").mt-4
        v-col
          v-row.justify-center
            v-col(sm="6" md="6")
              v-row.pa-2.justify-center.title.font-weight-regular
                v-icon(left) mdi-newspaper
                | News
              NewsTable( v-if="boards.edges.find(({node})=>node.pastNews.edges.length)"
                :newsList="boards.edges.flatMap(({node})=>node.pastNews.edges)"
              )
              v-col(v-else).text-center.title
                | There is no News.
            v-col(md="6" sm="6")
              v-row.pa-2.justify-center.title.font-weight-regular.text-center
                v-icon(left) mdi-note-text
                | Upcoming Events
              EventTable(
                v-if="boards.edges.find(({node})=>node.upcomingEvents.edges.length)"
                :eventsList="boards.edges.flatMap(({node}) => node.upcomingEvents.edges)"
              )
              v-col(v-else).text-center.title
                | There are no Upcoming Events.
    v-parallax(
      v-if="!$apollo.queries.festivals.loading"
      src="../assets/hero.jpeg"
      :height="$vuetify.breakpoint.smAndDown?'auto':carouselHeight"
    )
      v-content.align-center.mask
        v-container.container--fluid.mb-12
          v-row.display-1.justify-center.mb-12 Festivals
          v-row
            FestivalCarousel(:festivalsList="festivals.edges")
    v-container(v-if="!$apollo.queries.boards.loading")
      v-col(cols="12")
        p.display-1.text-center Boards
      v-col(cols="12" v-if="boards")
        v-row.justify-center
          v-col(cols="12" sm="6" v-for="({ node }, i) in boards.edges" :key="i")
            StripedCard(:node="node")
    v-container.pa-8
      v-card(class="accent white--text").elevation-10
        v-card-title.justify-center.display-1 Key People
    v-container(v-if="!$apollo.queries.senate.loading")
      v-row(v-for="({ node }, i) in senate.edges" :key="i").justify-space-around
        v-col(cols="12" md="4" v-if="node.genSecySenate")
          OfficeBearerCard(:avatarSize="120" :profile="node.genSecySenate" :designation="'General Secretary Student Senate'")
        v-col(cols="12" md="4" v-if="node.genSecyAcac")
          OfficeBearerCard(:avatarSize="120" :profile="node.genSecyAcac" :designation="'General Secretary ACAC'")
    v-img(src="../assets/other/background.svg" v-if="!$apollo.queries.homeGallery.loading && homeGallery" :min-height="carouselHeight")
      div.mask.fill-height
        v-container
          v-col(cols="12").text-center
            v-row.white--text.display-1.font-weight-light.justify-center.pa-10.ma-10 Memories
            CustomLightGallery(:images="homeGallery.photos.edges")
</template>

<script>
import { GET_BOARDS_QUERY } from "../graphql/queries/homeBoardQuery";
import { GET_FESTIVAL_QUERY } from "../graphql/queries/festivalQuery";
import FestivalCarousel from "../components/FestivalCarousel";
import StripedCard from "../components/common/cards/StripedCard";
import { GET_HOME_CAROUSEL_QUERY } from "../graphql/queries/homeCarouselQuery";
import NewsTable from "../components/common/tables/NewsTable";
import EventTable from "../components/common/tables/EventTable";
import { GET_HOME_GALLERY_QUERY } from "../graphql/queries/homeGalleryQuery";
import CustomLightGallery from "../components/common/CustomLightGallery";
import { GET_SENATE_DATA_QUERY } from "../graphql/queries/senateDataQuery";
import OfficeBearerCard from "../components/OfficeBearerCard";

export default {
  components: {
    CustomLightGallery,
    EventTable,
    NewsTable,
    StripedCard,
    FestivalCarousel,
    OfficeBearerCard
  },
  apollo: {
    boards: {
      query: GET_BOARDS_QUERY
    },
    festivals: {
      query: GET_FESTIVAL_QUERY
    },
    homeCarousel: {
      query: GET_HOME_CAROUSEL_QUERY
    },
    homeGallery: {
      query: GET_HOME_GALLERY_QUERY
    },
    senate: {
      query: GET_SENATE_DATA_QUERY
    }
  },
  data: () => ({
    carouselHeight: null
  }),
  methods: {
    onResize() {
      this.carouselHeight = window.innerHeight;
    }
  },
  mounted() {
    this.onResize();
  }
};
</script>
<style>
/*  very important do not delete this class*/
.v-parallax__content {
  padding: 0 !important;
}

.topbar-margin {
  margin-top: -48px;
}

.mask {
  background-color: rgba(0, 0, 0, 0.4);
}
</style>
