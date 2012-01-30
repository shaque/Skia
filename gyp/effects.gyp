{
  'includes': [
    'target_defaults.gypi',
  ],
  'targets': [
    {
      'target_name': 'effects',
      'type': 'static_library',
      'include_dirs': [
        '../include/config',
        '../include/core',
        '../include/effects',
      ],
      'sources': [
        '../include/effects/Sk1DPathEffect.h',
        '../include/effects/Sk2DPathEffect.h',
        '../include/effects/SkAvoidXfermode.h',
        '../include/effects/SkBlurDrawLooper.h',
        '../include/effects/SkBlurMaskFilter.h',
        '../include/effects/SkColorMatrix.h',
        '../include/effects/SkColorMatrixFilter.h',
        '../include/effects/SkCornerPathEffect.h',
        '../include/effects/SkDashPathEffect.h',
        '../include/effects/SkDiscretePathEffect.h',
        '../include/effects/SkDrawExtraPathEffect.h',
        '../include/effects/SkEmbossMaskFilter.h',
        '../include/effects/SkGradientShader.h',
        '../include/effects/SkGroupShape.h',
        '../include/effects/SkKernel33MaskFilter.h',
        '../include/effects/SkLayerDrawLooper.h',
        '../include/effects/SkLayerRasterizer.h',
        '../include/effects/SkPaintFlagsDrawFilter.h',
        '../include/effects/SkPixelXorXfermode.h',
        '../include/effects/SkPorterDuff.h',
        '../include/effects/SkRectShape.h',
        '../include/effects/SkTransparentShader.h',

        '../src/effects/Sk1DPathEffect.cpp',
        '../src/effects/Sk2DPathEffect.cpp',
        '../src/effects/SkAvoidXfermode.cpp',
        '../src/effects/SkBitmapCache.cpp',
        '../src/effects/SkBitmapCache.h',
        '../src/effects/SkBlurDrawLooper.cpp',
        '../src/effects/SkBlurMask.cpp',
        '../src/effects/SkBlurMask.h',
        '../src/effects/SkBlurMaskFilter.cpp',
        '../src/effects/SkColorFilters.cpp',
        '../src/effects/SkColorMatrixFilter.cpp',
        '../src/effects/SkCornerPathEffect.cpp',
        '../src/effects/SkDashPathEffect.cpp',
        '../src/effects/SkDiscretePathEffect.cpp',
        '../src/effects/SkEmbossMask.cpp',
        '../src/effects/SkEmbossMask.h',
        '../src/effects/SkEmbossMask_Table.h',
        '../src/effects/SkEmbossMaskFilter.cpp',
        '../src/effects/SkGradientShader.cpp',
        '../src/effects/SkGroupShape.cpp',
        '../src/effects/SkKernel33MaskFilter.cpp',
        '../src/effects/SkLayerDrawLooper.cpp',
        '../src/effects/SkLayerRasterizer.cpp',
        '../src/effects/SkPaintFlagsDrawFilter.cpp',
        '../src/effects/SkPixelXorXfermode.cpp',
        '../src/effects/SkPorterDuff.cpp',
        '../src/effects/SkRadialGradient_Table.h',
        '../src/effects/SkRectShape.cpp',
        '../src/effects/SkTransparentShader.cpp',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../include/effects',
        ],
      },
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2: