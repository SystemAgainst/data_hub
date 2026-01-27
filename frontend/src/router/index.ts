import { createRouter, createWebHistory } from 'vue-router'
import HubPage from '@/pages/HubPage.vue'
import { tokenName } from '@/api/http'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'hub',
      component: HubPage,
      meta: { layout: 'center', requiresAuth: true },
    },
    {
      path: '/auth',
      name: 'auth',
      component: () => import('@/pages/AuthPage.vue'),
      meta: { layout: 'center', guestOnly: true },
    },
    {
      path: '/projects',
      name: 'projects',
      component: () => import('@/pages/ProjectsPage.vue'),
      meta: { layout: 'projects', requiresAuth: true },
    },
    {
      path: '/projects/:id',
      name: 'project-detail',
      component: () => import('@/pages/ProjectDetailPage.vue'),
      meta: { layout: 'projects', requiresAuth: true },
    },
  ],
})

// ГЛОБАЛЬНАЯ ПРОВЕРКА ПЕРЕД КАЖДЫМ ПЕРЕХОДОМ
router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem(tokenName)

  // 1. Если страница требует авторизации, а мы не вошли
  if (to.meta.requiresAuth && !isAuthenticated) {
    // Редиректим на логин, но запоминаем, куда хотели попасть
    next({ name: 'auth', query: { redirect: to.fullPath } })
    return
  }

  // 2. Если мы уже вошли, нечего делать на странице логина
  if (to.meta.guestOnly && isAuthenticated) {
    next({ name: 'hub' })
    return
  }

  next()
})

export default router
