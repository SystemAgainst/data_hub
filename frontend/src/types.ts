// Описываем тип Проекта (как он приходит с бэка)
export interface Project {
  id: number
  title: string
  description: string
  cover_image?: string
  total_cost: number | string
  updated_at: string
  updated_by_name: string
  // participants пока пропустим, если их нет в serializer'е списка
}
