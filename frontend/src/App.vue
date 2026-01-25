<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import CenterLayout from '@/layouts/CenterLayout.vue'
import ProjectsLayout from '@/layouts/ProjectsLayout.vue'

const route = useRoute()
const layout = computed(() => {
  const layoutName = route.meta.layout || 'center'

  if (layoutName === 'projects') return ProjectsLayout
  return CenterLayout
})
</script>

<template>
  <component :is="layout">
    <RouterView />
  </component>
</template>

<style scoped></style>
