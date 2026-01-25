<script setup lang="ts">
import { useRouter } from 'vue-router'
import MenuButton from '@/components/ui/MenuButton.vue'

const router = useRouter()

// Функция навигации
const goTo = (route: string) => {
  router.push(route)
}
</script>

<template>
  <div class="space-y-4">
    <!-- Кнопка 1: Отчетность (Проекты) -->
    <MenuButton
      title="Отчетность"
      subtitle="Проекты, сметы, документы"
      @click="goTo('/projects')"
      style="cursor: pointer"
    >
      <!-- Можем заменить иконку на что-то тематическое -->
      <template #icon> 📄 </template>
    </MenuButton>

    <!-- Кнопка 2: Парсер (Заглушка пока) -->
    <MenuButton title="Парсер аварийного жилья" subtitle="Мониторинг площадок" :disabled="true">
      <template #icon> 🏢 </template>
    </MenuButton>

    <!-- Кнопка 3: Финансы (Заглушка) -->
    <MenuButton title="Сколько денег" subtitle="В разработке" :disabled="true" />
  </div>
</template>
