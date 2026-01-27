import api from './http'
import type { Project, ProjectStats } from '@/types'

export const getProjects = () => api.get<Project[]>('projects/')

export const getProjectById = (id: number) => api.get<Project>(`projects/${id}/`)

// Создать проект (на будущее). FormData нужен, если будем слать картинки
export const createProject = (data: FormData) =>
  api.post<Project>('projects/', data, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
export const updateProject = (id: number, data: Partial<Project>) =>
  api.patch<Project>(`projects/${id}/`, data)

export const deleteProject = (id: number) => api.del(`projects/${id}/`)

export const getProjectStats = (id: number | string) =>
  api.get<ProjectStats>(`projects/${id}/stats/`)
