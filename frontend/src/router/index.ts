import { createRouter, createWebHistory } from 'vue-router'
import HubPage from '@/pages/HubPage.vue'
import AuthPage from '@/pages/AuthPage.vue'
import ProjectsPage from '@/pages/ProjectsPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'hub',
      component: HubPage,
      meta: { layout: 'center' },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/pages/AuthPage.vue'),
      meta: { layout: 'center' },
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('@/pages/ProjectsPage.vue'),
      meta: { layout: 'projects' },
    },
  ],
})

export default router
