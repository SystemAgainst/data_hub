<script setup lang="ts">
defineProps<{
  title: string
  icon?: string
  badge?: string | number
  clickable?: boolean
  externalLink?: string
}>()
</script>

<template>
  <div
    class="bg-dark-surface relative flex h-full flex-col rounded-xl border border-white/5 p-4 transition-colors"
    :class="{ 'hover:border-primary/50 cursor-pointer': clickable }"
  >
    <!-- Шапка -->
    <div class="mb-3 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span v-if="icon" class="text-2xl">{{ icon }}</span>

        <!-- Если есть ссылка, делаем заголовок ссылкой -->
        <a
          v-if="externalLink"
          :href="externalLink"
          target="_blank"
          rel="noopener noreferrer"
          class="hover:text-primary flex items-center gap-1 font-medium text-white decoration-dashed underline-offset-4 transition-colors hover:underline"
          @click.stop
        >
          {{ title }}
          <!-- Иконка внешней ссылки (стрелочка) -->
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="opacity-50"
          >
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
            <polyline points="15 3 21 3 21 9"></polyline>
            <line x1="10" y1="14" x2="21" y2="3"></line>
          </svg>
        </a>

        <!-- Иначе просто текст -->
        <h4 v-else class="font-medium text-white">{{ title }}</h4>
      </div>

      <span v-if="badge" class="text-dark-muted rounded-md bg-white/5 px-2 py-1 text-xs">
        {{ badge }}
      </span>
    </div>

    <div class="flex-1">
      <slot />
    </div>
  </div>
</template>
