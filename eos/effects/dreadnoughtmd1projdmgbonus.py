# dreadnoughtMD1ProjDmgBonus
#
# Used by:
# Ship: Naglfar
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("dreadnoughtShipBonusM1"), skill="Minmatar Dreadnought")
