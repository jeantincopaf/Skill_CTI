# Scoping Review CTI

Skill para Codex orientada a planificar, documentar y ejecutar revisiones de
alcance sobre evidencia empírica de políticas y estrategias de ciencia,
tecnología e innovación (CTI) en salud y medicina.

## Alcance inicial

- Marco: PCC, JBI y PRISMA-ScR.
- Objeto principal: políticas, estrategias, programas e intervenciones de CTI
  en salud o medicina.
- Evidencia: estudios empíricos y documentos de políticas/estrategias con
  evidencia observable.
- Propiedad intelectual: dimensión secundaria; se registran patentes,
  licenciamiento, transferencia tecnológica y acceso cuando aparecen, pero no
  son requisitos de inclusión.
- Revisores: R1 es la IA y R2 es una persona investigadora. La persona debe
  validar el corpus final y adjudicar desacuerdos.
- Exclusiones: estudios puramente conceptuales o teóricos, innovación social sin
  componente tecnológico/CTI y estudios de evaluación de tecnologías sanitarias
  sin análisis de política o CTI.
- Por defecto no se limitan fecha, idioma ni geografía; cualquier filtro usado
  debe registrarse en el historial de búsqueda.

## Instalación en Codex

Clona este repositorio en la carpeta de skills de Codex o copia su contenido
como una skill llamada `scoping-review-cti`. La entrada principal es
`SKILL.md`. El archivo `agents/openai.yaml` contiene los metadatos de interfaz.

## Modos de trabajo

1. `intake`: PCC, preguntas, objetivos y criterios de elegibilidad.
2. `search`: ecuaciones por base de datos y registro reproducible de búsquedas.
3. `screen`: deduplicación, piloto, cribado IA–humano y adjudicación.
4. `extract`: matriz de extracción con localizadores de evidencia.
5. `synthesize`: mapas de países, actores, instrumentos, ciclo de política,
   resultados y dimensión secundaria de propiedad intelectual.
6. `report`: conteos PRISMA-ScR, razones de exclusión y texto de métodos/resultados.

## Archivos incluidos

- `references/`: metodología, ecuaciones, esquema de extracción y artefactos
  PRISMA-ScR.
- `assets/`: plantillas CSV y workbook XLSX para cribado, texto completo,
  extracción, búsquedas y PRISMA.
- `scripts/`: validación del cribado y cálculo de conteos PRISMA.

## Límites metodológicos

La skill puede proponer búsquedas, clasificar registros provisionalmente y
preparar matrices. No debe presentar una ecuación como búsqueda ejecutada ni
llamar efectiva a una política sin evidencia empírica. Las decisiones finales
de inclusión, exclusión, adjudicación e interpretación requieren validación
humana.

