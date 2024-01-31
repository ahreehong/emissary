{{/* Generate image repository path. */}}
{{- define "image.repository.path" -}}
{{- .repository }}@{{ .digest -}}
{{- end -}}
