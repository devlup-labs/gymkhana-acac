<template lang="pug">
v-flex
  v-parallax.topbar-style(
    dark,
    :src="require('../assets/hero.jpeg')",
    :height="$vuetify.theme.options.parallaxHeight"
  )
    v-layout.justify-center.align-center.fill-height.ma-8
      h1 Festivals
  v-container
    v-row.justify-center(
      :style="{ 'margin-top': `20px` }",
      v-for="({ node }, i) in festivals.edges",
      :key="i",
      :class="(i + 1) % 2 == 0 ? 'ml-8' : 'mr-8'"
    )
      v-col.pb-4.pt-0(sm="10")
        v-card.pa-2.ma-1.elevation-8(
          :style="{ 'border-top': `8px solid ${$vuetify.theme.themes.light.primary}` }"
        )
          v-row
            v-col(md="4")
              v-img.ma-2.pa-0.rounded-circle(
                :src="node.photo.sizes.find((e) => e.name === 'full_size').url",
                max-height="250",
                max-width="250"
              )
            v-col.pl-0.pt-8
              v-card-title.display-1.mb-2 {{ node.name }}
              v-card-subtitle.black--text {{ node.tagLine }}
              v-card-text
                span(v-html="node.about")
              v-card-actions.justify-end(v-if="")
                | Link to Page
                v-btn.ml-2.accent(
                  right,
                  ripple,
                  :href="node.link",
                  target="_blank"
                )
                  v-icon mdi-arrow-right
    .pa-8
</template>

<script>
import Footer from "../components/common/Footer";
import { GET_FESTIVAL_QUERY } from "../graphql/queries/festivalQuery";

export default {
  apollo: {
    festivals: {
      query: GET_FESTIVAL_QUERY,
    },
  },
  name: "Festival",
  components: {
    Footer,
  },
  data: () => ({
    tab: null,
  }),
};
</script>

<style scoped>
.topbar-style {
  margin-top: -48px;
}

.background-color {
  background-color: #fafafa;
}

.rounded-circle {
  border-radius: 100%;
}
</style>
